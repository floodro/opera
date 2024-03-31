from django.shortcuts import render

# Create your views here.
def enterDashboard(response):
    return render(response,'dashboard.html', {})

def enterLanding(response):
    return render(response, 'landing.html', {})

