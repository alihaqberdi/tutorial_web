from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.forms import UserCreationForm
from . import forms
# Create your views here.


def UserSignupView(request):
    userform = forms.UserForm()
    context = {'usercreate': userform}
    if request.method == "POST":
        userform = forms.UserForm(request.POST, request.FILES)
        if userform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()
        return HttpResponseRedirect(reverse('login'))
    return render(request, 'registration/signup.html', context)

