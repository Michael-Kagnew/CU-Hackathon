from django.shortcuts import render, redirect

def index(request):
    if not check_auth(request):
        return redirect('signin')

    return render(request, 'contracts.html')

def check_auth(request):
    if not request.user.is_authenticated:
        return False
    else:
        return True
