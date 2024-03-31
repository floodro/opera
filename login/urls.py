from django.urls import path
from . import views as v2

urlpatterns= [
    path("", v2.userLogin, name="login"),
    path("", v2.userRegister, name="register")
]
