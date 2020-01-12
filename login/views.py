from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .forms import SigninForm, SignupForm

from profiles.models import Consultant, Client
from profiles.views import get_profile_status

def index(request):
    if not check_auth(request):
        return redirect('signin')

    print('dashboard')

    # check profile type
    if not request.user.is_superuser:
        profile, ref, status = get_profile_status(request)

        if not status:
            print('Profile needs to be created')
            return redirect('edit_profile')

    return render(request, 'index.html')

def signin(request):
    print('signin')

    if request.method == 'POST':
        form = SigninForm(request.POST)

        if form.is_valid():
            raw_password = form.cleaned_data['password']
            raw_username = form.cleaned_data['username']

            user = authenticate(username=raw_username, password=raw_password)

            if user is None:
                return redirect('signup')

            login(request, user)

            print('woah, user signed in')

            return redirect('/index')
    else:
        form = SigninForm()

    return render(request, 'signin.html', {'form': form})

def signup(request):
    print('signin')

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = form.cleaned_data['account_type']
            email = form.cleaned_data['email']

            if account_type == 'Consultant':
                # consultant profile
                consultant = Consultant()
                consultant.user = user
                consultant.email = email
                consultant.save()
            else:
                # client profile
                client = Client()
                client.user = user
                client.email = email
                client.save()

            raw_password = form.cleaned_data['password1']
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('index')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')

# HELPERS
def check_auth(request):
    if not request.user.is_authenticated:
        return False
    else:
        return True
