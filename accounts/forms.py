from django.contrib.auth.forms import forms
from .models import CustomUser
from django.contrib.auth.models import User
#
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = 'username', 'first_name', 'password'
        widgets = {
            'password': forms.PasswordInput(),
        }





# class CustomUserChangeForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = 'username', 'first_name', 'last_name', 'img'
# #
#
#
