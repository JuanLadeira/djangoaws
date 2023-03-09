from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect, render

from .forms import CreateUserForm, LoginForm, UpdateUserForm
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
@login_required(login_url="example:my-login")
def my_dashboard(request):
    return render(request, 'example/dashboard.html', {})

@login_required(login_url="example:my-login")
def profile_management(request):
    form = UpdateUserForm(instance=request.user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('example:dashboard')

    return render(request, 'example/profile-management.html', {'form': form})

def user_logout(request):
    auth.logout(request)
    return redirect("example:homepage")

@login_required(login_url="example:my-login")
def delete_conta(request):
    if request.method == "POST":
        deleteUser  = User.objects.get(username=request.user)
        deleteUser.delete()
        return redirect("example:homepage")
    
    return render(request, "example/deleteconta.html", {})