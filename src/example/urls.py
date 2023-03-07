from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.index, name=""),
    path('register', views.register, name = "register"),
    path('my-login', views.my_login, name = "my-login"),
    path('dashboard', views.my_dashboard, name = "my-dashboard"),
    path('profile-management', views.profile_management, name = "profile-management"),

]