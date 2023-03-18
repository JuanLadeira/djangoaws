from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):    
    profile_pic = models.ImageField(upload_to='images/', null=True, blank=True, default='images/avatar.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username