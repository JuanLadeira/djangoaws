from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from .models import Profile


#user registration
class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class UpdateUserForm(forms.ModelForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'email']
        exclude = ['password1', 'password2']

class UpdateProfileForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control-file'}))
    class Meta:
        model = Profile
        fields =  ['profile_pic']
      