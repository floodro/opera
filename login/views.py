from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def renderLogin(request):
    if request.method == "POST":

        isVerified = False
        isLoggedIn = False

        sr_code = request.POST.get('sr_code')
        password = request.POST.get('password')

        user = user_collection.find_one({'sr_code': sr_code, 'password': password})

        if user:
            isLoggedIn = True

            if isLoggedIn == True:
                return redirect('dashboard')

        else:
            return render(request, 'login-performer.html', {'error_message': "Invalid username / password!"})
    else:
        return render(request, 'login-performer.html', {})

def renderLoginAsAdmin(request):
    return render(request, 'login-admin.html')

def renderSignup(request):
    return render(request, 'signup-performer.html', {})

def renderLanding(request):
    return render(request, 'landing.html', {})

def submit_form(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        sr_code = request.POST.get('sr_code')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        campus = request.POST.get('campus')
        college = request.POST.get('college')
        cultural_group = request.POST.get('cultural_group')

        if password != confirm_password:
            return HttpResponse("Passwords do not match!", status=400)

        new_user = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'sr_code': sr_code,
            'password': password,
            'campus': campus,
            'college': college,
            'cultural_group': cultural_group
        }

        user_collection.insert_one(new_user) #Insert new user into the MongoDB collection using the model

        return redirect('user_login')
    
    else:  
        return HttpResponse('Method not allowed', status=400)
