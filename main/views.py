from django.shortcuts import render

# Create your views here.
def landing(response):
    return render(response,'dashboard.html', {})