from django.urls import path
from .views import UserRegisterView
from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    #path('login/', views.login_view, name='login'),
    ]
