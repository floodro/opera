from django.shortcuts import render, redirect
from .models import office_metrics

# Create your views here.
def enterDashboard(request):
    return render(request,'dashboard-director.html', {})

def enterLanding(request):
    return render(request, 'about-us.html', {})

def contact(request):
    return render(request, 'contact-us.html', {})

def enterForms(request):
    return render(request, 'forms.html', {})

def enterEvents(request):
    return render(request, 'events.html', {})

def managePerformer(request):
    return render(request, 'manage-performer.html', {})

def performerProfile(request):
    return render(request, 'performer-profile.html', {})

def enterReports(request):
    return render(request, 'reports.html', {})

def enterRecognition(request):
    return render(request, 'recognition-view.html', {})

def updateProfile(request):
    
    if isVerified == True:
        updated_first_name = request.POST.get('first_name')
        updated_last_name = request.POST.get('last_name')
        updated_email = request.POST.get('email')
        updated_sr_code = request.POST.get('sr_code')
        updated_password = request.POST.get('password')
        updated_confirm_password = request.POST.get('confirm_password')
        updated_campus = request.POST.get('campus')
        updated_college = request.POST.get('college')
        updated_cultural_group = request.POST.get('cultural_group')

    updated_user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'sr_code': sr_code,
        'password': password,
        'campus': campus,
        'college': college,
        'cultural_group': cultural_group
    }