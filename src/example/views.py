from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.shortcuts import redirect, render

from .forms import CreateUserForm, LoginForm
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'example/index.html', {})


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            return redirect('example:my-login')
    return render(request, 'example/register.html', {'form': form})

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("example:dashboard")
    
    return render(request, 'example/mylogin.html', {'form': form})

def my_dashboard(request):
    return render(request, 'example/dashboard.html', {})

def profile_management(request):
    return render(request, 'example/profile-management.html', {})

def user_logout(request):
    auth.logout(request)
    return redirect("homepage")