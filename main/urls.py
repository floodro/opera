from django.urls import path
from . import views

urlpatterns= [
    path("dashboard/", views.enterDashboard, name="dashboard"),
    path("", views.enterLanding, name="landing"),
    path("home/", views.enterHome, name="home"),
]