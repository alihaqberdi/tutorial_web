from django.db import models
from django.contrib.auth.models import AbstractUser
# from tutorial.models import Product

# Create your models here.


class CustomUser(AbstractUser):
    profile_img = models.ImageField(upload_to='profile_img', default='anonm.jpg')



class Profile(models.Model):
    user = models.OneToOneField('accounts.CustomUser', related_name='profile', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200 , blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    info = models.CharField(max_length=2000, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to='profile',default='anonm.jpg')
    product = models.ManyToManyField('tutorial.Product')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
