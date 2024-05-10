from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
import pymysql

def renderLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_data = authenticate_user(email, password)
        
        if user_data:
            # Assuming 'dashboard' is the name of your dashboard view
            # Redirect to dashboard upon successful login
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid email or password.")
    
    return render(request, 'login.html', {})

def userLogout(request):
    logout(request)
    return redirect('user_landing')

def renderSignup(request):
    return render(request, 'signup.html', {})

def renderLanding(request):
    return render(request, 'landing.html', {})

def submit_form(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        sr_code = request.POST.get('sr_code')
        campus = request.POST.get('campus')
        cultural_group = request.POST.get('cultural_group')
        
        if password1 == confirm_password:
            user = User(
                email=email, 
                password1=password1, 
                confirm_password=confirm_password, 
                first_name=first_name, 
                last_name=last_name, 
                sr_code=sr_code,
                campus=campus)
            
            user.save()
        
            print("Data successfully saved!")
            return redirect('user_login')  # Redirect to login page after successful form submission
        
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'signup.html', {})

def authenticate_user(email, password):
    connection = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='Floodroplays09',
                                 database='opera',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM accounts WHERE email = %s AND password1 = %s"
            cursor.execute(sql, (email, password))
            user_data = cursor.fetchone()

            if user_data:
                return user_data
            else:
                return None
    finally:
        # Close the database connection
        connection.close()
