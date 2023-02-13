from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','id', 'first_name', 'last_name', 'password', 'is_staff', 'is_active', 'profile_img']

@admin.register(Profile)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['user','name', 'username', 'location', 'update']

