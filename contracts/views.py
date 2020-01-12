from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContractForm
from .models import Contract

from profiles.models import Consultant, Client

prof_type = [Consultant, Client]

def index(request):
    if not check_auth(request):
        return redirect('signin')
    
    profile, ref = get_profile(request)

    contracts = Contract.objects.filter(client=profile)

    context = {
        "contracts": contracts
    }

    return render(request, 'contracts.html', context=context)

def create_contract(request):
    profile, ref = get_profile(request)

    if ref == 0:
        return redirect("index")

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

    context = {
        'contract': contract
    }

    return render(request, 'view_contract.html', context=context)

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
