from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .helpers import send_forget_password_token

# index/ home page function


def index(request):
    return render(request, 'index.html')


# About Us Page function
def about(request):
    return render(request, 'aboutus.html')


# Press Page Function
def press(request):
    return render(request, 'press.html')

# Privacy Page function


def privacy(request):
    return render(request, 'privacy.html')


# Terms and Conditions Page function
def terms(request):
    return render(request, 'tnc.html')


# Contact Us Page Function
def contact(request):
    return render(request, 'contact.html')


# FAQ Page function
def faq(request):
    return render(request, 'faq.html')


# Dashboard Page function
def dashboard(request):
    return render(request, 'dashboard.html')

# logout function


def handlelogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/')


# Login Function
def login(request):
    if request.method == 'POST':
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpassword')

        user_obj = User.objects.filter(
            username=username, password=password).first()
        user = authenticate(username=username, password=password)
        if user_obj is None:
            messages.error(request, 'Invalid username')
            return redirect('/')

        profile_obj = Profile.objects.filter(user__username=username).first()
        if not profile_obj.isVerified:
            messages.error(request, 'Account not verified. Check your mail')
            return redirect('/')

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials! Please Try Again')
            return redirect('/')

    return HttpResponse('login')


# SignUp Function
def signup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        confpassword = request.POST.get('confpassword')
        if User.objects.filter(username=username).first():
            messages.success(request, 'Username already exists')
            return redirect(request, '/')
        if len(str(username)) < 6:
            messages.error(
                request, 'Username must be atleast 6 characters')
            return redirect('/')
        if not username.isalnum():
            messages.error(
                request, 'Username should contain only letters and numbers')
            return redirect('/')
        if User.objects.filter(email=email).first():
            messages.success(request, 'Email already exists')
            return redirect(request, '/')
        if password != confpassword:
            messages.error(request, 'Password does not match')
            return redirect('/')
            # Create the user
        user_obj = User(name, username, email)
        user_obj.set_password(password)
        user_obj.save()
        auth_token = str(uuid.uuid4())
        profile_obj = Profile(user=user_obj, auth_token=auth_token)
        activate_account(email, auth_token)
        profile_obj.save()
        messages.success(
            request, " Your account has been successfully created")
        messages.success(
            request, " Check your email and verify your account")
    else:
        return HttpResponse("404 - Page Not Found")
    return HttpResponse('signup')


# activate account function
def activate_account(email, token):
    subject = 'Activate your account'
    message = f'Hi, verify your account: http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)


# verification function
def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filters(auth_token=auth_token)
        if profile_obj:
            if profile_obj.isVerified:
                messages.success(request, 'Account already activated')
                return redirect('/login')
            profile_obj.isVerified = True
            profile_obj.save()
            messages.success(request, 'Account verified successfully')
            return redirect('/login')
        else:
            messages.success(request, 'Invalid token')
            return redirect('/')
    except Exception as e:
        print(e)


# error function
def error(request):
    return render(request, 'error.html')


# forget password
def forget_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')

            user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.error(request, 'No user found')
            return redirect('/forget-password')
        token = str(uuid.uuid4())
        user_obj = User.objects.get(username=username)
        profile_obj = Profile.objects.get(user=user_obj)
        profile_obj.forget_password_token = token
        profile_obj.save()
        send_forget_password_token(user_obj, token)
        messages.error(request, 'Reset Password Sent')
        return redirect('/login')
    except Exception as e:
        print(e)
    return render(request, 'registration/forget.html')


# change password
def change_password(request, token):
    context = {}
    try:
        profile_obj = Profile.objects.filter(
            forget_password_token=token).first()
        context = {'user_id': profile_obj.user.id}
        if request.method == 'POST':
            new_password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.error(request, 'No user id found')
                return redirect('/change-password/{token}')
            user_obj = User.objects.get(id=user_id)
            if new_password != confirm_password:
                messages.error(request, 'Password does not match')
                return redirect('/change-password/{token}')
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/login')

    except Exception as e:
        print(e)

    return render(request, 'registration/change_password.html', context)
