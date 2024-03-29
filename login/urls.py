from django.urls import path
from . import views as v2

urlpatterns= [
    path("", v2.login, name="login")
]
