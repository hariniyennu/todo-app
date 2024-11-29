from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully")
                return redirect('login')
        else:
            messages.error(request,"Passwords do not match")
    return render(request,'myapp/todo.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Login attempt: username={username}, password={password}") 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            print(f"Login successful for user: {user.username}")
            return redirect('to_do') 
        else:
            print("Invalid login attempt")
            messages.error(request, "Invalid username or password")
    else:
        print(f"GET request at login_view: {request.path}") 
    return render(request, 'myapp/signup.html')  
def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            subject = "Password Reset Requested"
            message = "Click the link below to reset your password."
            email_content = f"{message} /reset-password/{user.pk}/{default_token_generator.make_token(user)}/"
            send_mail(subject, email_content, 'noreply@example.com', [email])
            messages.success(request, "Password reset link sent. Check your email.")
        else:
            messages.error(request, "No account found with that email.")
        return redirect('forgot_password')
    return render(request, 'myapp/forgot_password.html')
def to_do(request):
    print(f"to_do view accessed by: {request.user}")
    if request.user.is_authenticated:
        print(f"User {request.user.username} is authenticated, rendering todo.html")
        return render(request,'myapp/todo.html')  
    else:
        print("Unauthenticated user trying to access to_do, redirecting to login")
        return redirect('login')
def main(request):
    if request.user.is_authenticated:
        return redirect('to_do')
    else:
        return redirect('login')  
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
