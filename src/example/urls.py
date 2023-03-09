from django.urls import path

from . import views

app_name='example'

urlpatterns = [ 
    path('', views.index, name="homepage"),
    path('register', views.register, name="register"),
    path('my-login', views.my_login, name="my-login"),
    path('user-logout', views.user_logout, name='user-logout'),
    path('dashboard', views.my_dashboard, name="dashboard"),
    path('profile-management', views.profile_management, name="profile-management"),
    path('delete-conta', views.delete_conta, name='delete-conta')
]