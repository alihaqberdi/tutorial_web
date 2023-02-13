from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import CustomUser, Profile
from . import forms
from django.db.models.signals import post_save, post_delete
from django.dispatch import Signal, receiver
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.




def ProfileView(request):
    product = request.user.profile

    context = {
        'profile': product
    }
    return render(request, 'accounts/account.html', context)

def UserSignupView(request):
    userform = forms.UserForm()
    context = {'usercreate': userform}
    if request.method == "POST":
        userform = forms.UserForm(request.POST)
        if userform.is_valid() and request.POST['confirm_password'] == request.POST['password']:
            user = userform.save()
            user.username = user.username.lower()
            user.set_password(user.password)
            user.save()
            messages.success(request,'muvaffaqiyatli ro\'yxatdan o\'tildi')
            return redirect('accounts:login')
        else:
            messages.error(request,'xato malumotlarni tekshiring')


    return render(request, 'accounts/signup.html', context)


def LoginView(request):
    if request.user.is_authenticated:
        return redirect('tutorial:blog')
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request,'Muvafaqqiyatli')
            login(request, user)
            return redirect('tutorial:blog')
        else:
            messages.error(request,'bundey foydalanuvchi mavjud emas')
    return render(request, 'accounts/login.html')


def LogoutView(request):
    messages.info(request, 'tizimdan chiqdingiz')
    logout(request)
    return redirect('tutorial:blog')


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwards):
    # print(f"sender {sender}\nintance {instance}\ncreated {created}")
    if created:
        Profile.objects.create(
            user=instance
        )
    else:
        profi = Profile.objects.get(user=instance)
        profi.name = instance.first_name+' '+instance.last_name
        profi.username = instance.username
        profi.save()


@receiver(post_delete, sender=Profile)
def ProfileDelite(sender, instance, **kwargs):
    user = instance.user
    user.delete()



