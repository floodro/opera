from django.urls import path
from . import views

urlpatterns= [
    path("dashboard/", views.enterDashboard, name="dashboard"),
<<<<<<< HEAD
=======
    path("", views.enterLanding, name="landing"),
    path("home/", views.enterHome, name="home"),
>>>>>>> 49bae6a9c55ac4f64261c6065e5abeed06b112de
]