from django.shortcuts import render

from .forms import UserCreationForm


# Create your views here.
def index(request):
    return render(request, 'example/index.html', {})


def register(request):
    form = UserCreationForm
    return render(request, 'example/register.html', {'form': form})

def my_login(request):
    return render(request, 'example/mylogin.html', {})

def my_dashboard(request):
    return render(request, 'example/dashboard.html', {})

def profile_management(request):
    return render(request, 'example/profile-management.html', {})
    