from django.urls import path
from . import views as v2

urlpatterns= [
    path("login/", v2.renderLogin, name="user_login"),
    path("signup/", v2.renderSignup, name="user_signup"),
    path("landing/", v2.renderLanding, name="user_landing"),
    path("submit/", v2.submit_form, name="submit_form"),
    path("authenticate/", v2.authenticate_user, name="auth")
]
