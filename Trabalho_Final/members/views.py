### Código adaptado da playlist do canal Codemy: https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi ###
from django.shortcuts import render

from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name =  "registration/register.html"
    success_url = reverse_lazy("login")