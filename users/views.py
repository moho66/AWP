from re import template
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


# class login_view(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'login.html'
#     success_url = reverse_lazy('home')


def login_view(request):
    if  request.method =='POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm()

    return render(request,'users/templets/registration/login.html', {'form' : form })
    