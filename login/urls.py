from django.urls import path
from . import views as v2

urlpatterns= [
    path("login/", v2.userLogin, name="login"),
    path("register/", v2.userRegister, name="register")
]
