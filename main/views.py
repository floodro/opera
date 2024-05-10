from django.shortcuts import render, redirect

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
    pass