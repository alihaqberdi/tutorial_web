from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupView, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('profile/', views.ProfileView, name='profile'),
]