from django.shortcuts import render

# Create your views here.
def userLogin(response):
    return render(response, 'login.html', {})

def userRegister(response):
    return render(response, 'register.html', {})