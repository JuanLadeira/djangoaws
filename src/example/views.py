from django.shortcuts import redirect, render

from .forms import CreateUserForm
from .models import Profile


# Create your views here.
def index(request):
    return render(request, 'example/index.html', {})


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            current_user = form.save(commit=False)
            form.save()
            profile = Profile.objects.create(user=current_user)
            return redirect('my-login')
    return render(request, 'example/register.html', {'form': form})

def my_login(request):
    return render(request, 'example/mylogin.html', {})

def my_dashboard(request):
    return render(request, 'example/dashboard.html', {})

def profile_management(request):
    return render(request, 'example/profile-management.html', {})
    