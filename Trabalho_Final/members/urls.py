### Código adaptado da playlist do canal Codemy: https://www.youtube.com/watch?v=B40bteAMM_M&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi ###
from django.urls import path
from .views import UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
]
