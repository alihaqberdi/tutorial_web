from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.


class CustomUser(AbstractUser):
    profile_img = models.ImageField(upload_to='profile_img', default='anonm.jpg')