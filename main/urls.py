from django.urls import path
from . import views

urlpatterns= [
    path("dashboard/", views.enterDashboard, name="dashboard"),
    path("", views.enterLanding, name="landing"),
    path("contact/", views.contact, name="contact"),
    path("events/", views.enterEvents, name="events"),
    path("forms/", views.enterForms, name="forms"),
    path("manage/", views.managePerformer, name="manage"),
    path("profile/", views.performerProfile, name="profile"),
    path("reports/", views.enterReports, name="reports"),
    path("recognition/", views.enterRecognition, name="recognition")
]