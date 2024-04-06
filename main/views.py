from django.shortcuts import render

# Create your views here.
def enterDashboard(response):
    return render(response,'dashboard.html', {})


def enterHome(response):
    return render(response, 'home.html', {})

