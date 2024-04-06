from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def renderLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = user_collection.find_one({'username': username, 'password': password})

        if user:
            return redirect('dashboard')

        else:
            return render(request, 'login.html', {'error_message': "Invalid username / password!"})
    else:
        return render(request, 'login.html', {})

def renderSignup(request):
    return render(request, 'signup.html', {})

def renderLanding(request):
    return render(request, 'landing.html', {})

def submit_form(request):
    if request.method == "POST":
        sr_code = request.POST.get('sr_code')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        if password != confirm_password:
            return HttpResponse("Passwords do not match!", status=400)

        new_user = {
            'sr_code': sr_code,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }
    
        user_collection.insert_one(new_user) #Insert new user into the MongoDB collection using the model

        return redirect('user_login')
    
    else:  
        return HttpResponse('Method not allowed', status=400)
