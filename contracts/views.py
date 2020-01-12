from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect

from .forms import ContractForm
from .models import Contract

from profiles.models import Consultant, Client

prof_type = [Consultant, Client]

def index(request):
    if not check_auth(request):
        return redirect('signin')

    profile, ref = get_profile(request)
    msg = 0

    if ref == 1: 
        # Search contract for clients
        contracts = Contract.objects.filter(client=profile).filter(status="Open")
        pending = []
        completed = Contract.objects.filter(client=profile).filter(status="Closed")

    elif ref == 0:
        # search for contract for consultants
        contracts = []
        pending = []
        completed = []

        for contract in Contract.objects.all():
            if profile in contract.team.all():
                contracts.append(contract)

            elif profile in contract.applicants.all():
                pending.append(contract)

        if len(contracts) == 0:
            msg = 'No contracts yet.'

    context = {
        "contracts": contracts,
        "pending": pending,
        "completed": completed,
        "all_contracts": Contract.objects.all(),
        "ref": ref,
        'msg': msg
    }

    return render(request, 'contracts.html', context=context)

def create_contract(request):
    profile, ref = get_profile(request)

    if ref == 0:
        return redirect(index)

    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            new_contract = form.save(commit=False)
            new_contract.client = profile
            new_contract.status = "Open"
            new_contract.save()
            return redirect(index)
    else:
        form = ContractForm()

    return render(request, "contract_form.html", {'form': form})

def view_contract(request, id):
    contract = get_object_or_404(Contract, pk=id)
    profile, ref = get_profile(request)

    status = 0
    if contract.status == "Closed":
        status = 1

    context = {
        'contract': contract,
        'msg': '',
        'ref': ref,
        'status': status
    }

    if ref == 0:
        if profile in contract.team.all():
            context['msg'] = 'You are on the team.'
        elif profile in contract.applicants.all():
            context['msg'] = 'You have already applied to this position.'
        else:
            context['msg'] = 1
    else:
        context['applicants'] = contract.applicants.all()
        context['team'] = contract.team.all()

    return render(request, 'view_contract.html', context=context)

def apply(request, id):
    contract = get_object_or_404(Contract, pk=id)
    profile, ref = get_profile(request)

    contract.applicants.add(profile)

    return redirect(index)

def approve(request, id):
    consultant = get_object_or_404(Consultant, pk=id)
    profile, ref = get_profile(request)

    contracts = Contract.objects.filter(client=profile)

    for contract in contracts:
        if consultant in contract.applicants.all():
            contract.team.add(consultant)
            contract.applicants.remove(consultant)
            break

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def complete(request, id):
    contract = get_object_or_404(Contract, pk=id)

    contract.status = "Closed"
    contract.save()

    return redirect(index)

# HELPERS
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
