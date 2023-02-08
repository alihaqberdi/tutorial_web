from django.contrib.auth.forms import forms
from .models import CustomUser
from django.contrib.auth.models import User
#
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = 'username', 'first_name', 'last_name', 'email', 'password','profile_img'
        widgets = {
            'password': forms.PasswordInput()
        }





# class CustomUserChangeForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = 'username', 'first_name', 'last_name', 'img'
# #
#
#
