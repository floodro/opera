from django.urls import path
from . import views

urlpatterns= [
    path("", views.enterDashboard, name="dashboard"),
    path("", views.enterLanding, name="landing")
]
