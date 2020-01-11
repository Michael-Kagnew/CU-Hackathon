from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import SigninForm, SignupForm

def index(request):
    if not check_auth(request):
        return redirect('signin')

    print('login')

    return render(request, 'index.html')

def signin(request):
    print('signin')

    if request.method == 'POST':
        form = SigninForm(request.POST)

        if form.is_valid():
            raw_password = form.cleaned_data['password']
            raw_username = form.cleaned_data['username']

            user = authenticate(username=raw_username, password=raw_password)
            login(request, user)

            print('woah, user signed in')

            return redirect('index')
    else:
        form = SigninForm()

    return render(request, 'signin.html', {'form': form})

def signup(request):
    print('signin')

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            raw_password = form.cleaned_data['password1']
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('index')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

# HELPERS
def check_auth(request):
    if not request.user.is_authenticated:
        return False
    else:
        return True
