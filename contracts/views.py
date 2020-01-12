from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    if not check_auth(request):
        return redirect('signin')

    return render(request, 'contracts.html')

# Helpers
def check_auth(request):
    if not request.user.is_authenticated:
        return False
    else:
        return True
