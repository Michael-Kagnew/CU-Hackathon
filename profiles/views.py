from django.shortcuts import render, redirect, get_object_or_404

from .models import Consultant, Client
from .forms import ConsultantForm, ClientForm


from .github_info import git_userinfo

prof_type = [Consultant, Client]
prof_forms = [ConsultantForm, ClientForm]
prof_forms_html = ['consultant_form.html', 'client_form.html']

# Create your views here.

def index(request):
    print('profiles')
    if not check_auth(request):
        return redirect('/index')

    # check profile type
    profile, ref, status = get_profile_status(request)

    if profile is None:
        print('Profile does not exist')
        return redirect('/index')

    if not status:
        print('Profile needs to be created')
        return redirect('edit_profile')

    return redirect('dashboard')

def edit_profile(request):
    profile, ref = get_profile(request)

    if request.method == 'POST':
        form = prof_forms[ref](request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = prof_forms[ref](instance=profile)

    return render(request, prof_forms_html[ref], {'form': form})

def view_profile(request, id):
    consultant = get_object_or_404(Consultant, pk=id)

    if git_userinfo(consultant.github_link) is not None:
        repos = git_userinfo(consultant.github_link)['Repositories']

        if repos is not None:
            if len(repos) > 5:
                repos = repos[0:5]
        else:
            repos = []
    else:
        repos = []

    skills = consultant.skills.all()        

    context = {
        'profile': consultant,
        'skills': skills,
        'repos': repos
    }

    return render(request, 'view_profile.html', context=context)

def dashboard(request):
    profile, ref = get_profile(request)

    if ref == 0:
        # Consultants
        if git_userinfo(profile.github_link) is not None:
            repos = git_userinfo(profile.github_link)['Repositories']

            if repos is not None:
                if len(repos) > 5:
                    repos = repos[0:5]
            else:
                repos = []
        else:
            repos = []

        context = {
            "name": profile.first_name + " " + profile.last_name,
            "email": profile.email,
            "status": profile.status,
            "bio": profile.bio,
            "linkedin": profile.linkedin_link,
            "github": profile.github_link,
            'repos': repos,
            "type": "consultant"
        }
    elif ref == 1:
        # Clients
        context = {
            "name": profile.company_name,
            "email": profile.email,
            "bio": profile.bio,
            "website": profile.website,
            "type": "client"
        }
    return render(request, 'profiles.html', context=context)

# Helpers
def get_profile(request):
    profile, ref, status = get_profile_status(request)

    return profile, ref

def get_profile_status(request):
    # will return profile, type, status
    # type refers to index of prof_type (0 means Consultant, 1 means Client)
    # status = false means account needs to be created

    status = False

    for i in range(len(prof_type)):
        query = prof_type[i].objects.filter(user=request.user)

        if len(query) != 0:
            if query[0].first_name != "":
                status = True

            return query[0], i, status

    return None, 0, status

def check_auth(request):
    if not request.user.is_authenticated:
        return False
    else:
        return True