from typing import ContextManager
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
import uuid
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .helpers import send_forget_password_token
from django.views.decorators.csrf import csrf_exempt


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
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# Dashboard Page function
@login_required
def dashboard_status(request):
    allObjects = BusinessProfile.objects.all()
    context = {'stats': allObjects}
    return render(request, 'dashboardstatus.html', context)


# logout function
def handlelogout(request):
    logout(request)
    return redirect('/')


# Login Function
@csrf_exempt
def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        # user_obj = User.objects.filter(
        #     username=username, password=password).first()
        user = authenticate(username=loginusername, password=loginpassword)
        # if user_obj is None:
        #     messages.error(request, 'Invalid username')
        #     return redirect('/')

        # profile_obj = Profile.objects.filter(user__username=username).first()
        # if not profile_obj.isVerified:
        #     messages.error(request, 'Account not verified. Check your mail')
        #     return redirect('/')

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials! Please Try Again')
            return redirect('/')


# SignUp Function
@csrf_exempt
def signup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confpassword = request.POST.get('confpassword')

        # Check errorness of the form
        # if User.objects.filter(username=username).first():
        #     messages.success(request, 'Username already exists')
        # if len(str(username)) < 6:
        #     messages.error(
        #         request, 'Username must be atleast 6 characters')
        # if not username.isalnum():
        #     messages.error(
        #         request, 'Username should contain only letters and numbers')
        # if User.objects.filter(email=email).first():
        #     messages.success(request, 'Email already exists')
        # if password != confpassword:
        #     messages.error(request, 'Password does not match')

        # Create the user
        user_obj = User.objects.create_user(username, password)
        user_obj.email = email
        user_obj.first_name = fname
        user_obj.last_name = lname
        user_obj.set_password(password)
        user_obj.save()
        auth_token = str(uuid.uuid4())
        # profile_obj = Profile(
        #     user=user_obj, auth_token=auth_token)
        # profile_obj.save()
        messages.success(
            request, " Your Firmingle account has been successfully created")
        messages.success(
            request, " Check your email and verify your account")

    else:
        return HttpResponse("404 - Page Not Found")

    return redirect('/')


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


# Business Profile Function
def profile(request):
    return render(request, 'profile/confidential.html')


# Business Function
def business(request):
    return render(request, 'profile/business.html')


# Business Function
def business1(request):
    return render(request, 'profile/business1.html')


# Business Function
def business2(request):
    return render(request, 'profile/business2.html')


# Plan Function
def plan(request):
    return render(request, 'profile/plan.html')


# Detailed Post Page
def detailPost(request):
    return render(request, 'browse/detail.html')


# Browse Business
def browseBusiness(request):
    allObjects = BusinessProfile.objects.all()
    context = {'allProfiles': allObjects}
    return render(request, 'browse/browse_business.html', context)


# Browse Investors
def browseInvestor(request):
    allObjects = InvestmentProfile.objects.all()
    context = {'allProfiles': allObjects}
    return render(request, 'browse/browse_investor.html', context)


# form submit
@csrf_exempt
def businessAdd(request):
    if request.method == "POST":
        # Get the post parameters
        confname = request.POST.get('confname')
        confcompany = request.POST.get('confcompany')
        confphone = request.POST.get('confphone')
        confemail = request.POST.get('confemail')
        confprof = request.POST.get('confprof')
        confdate = request.POST.get('confdate')
        confinterest = request.POST.get('confinterest')
        confloc = request.POST.get('confloc')
        confind = request.POST.get('confind')
        confhow = request.POST.get('confhow')
        conflegal = request.POST.get('conflegal')
        confdes = request.POST.get('confdes')
        conflist = request.POST.get('conflist')
        confhigh = request.POST.get('confhigh')
        confdesc1 = request.POST.get('confdes1')
        confsale = request.POST.get('confsale')
        confyear = request.POST.get('confyear')
        confprofit = request.POST.get('confprofit')
        confphy = request.POST.get('confphy')
        confassets = request.POST.get('confassets')
        chooseimage = request.POST.get('chooseimage')
        choosedocs = request.POST.get('choosedocs')
        choosefast = request.POST.get('choosefast')
        print(confname)
        biz_obj = BusinessProfile.objects.create(
            name=confname,
            email=confemail,
            phone=confphone,
            profession=confprof,
            business_established=confdate, 
            business_location=confloc, 
            industry=confind, 
            interested_in=confinterest, 
            company=confcompany, 
            no_employees=confhow, 
            legal=conflegal, 
            describe=confdes, 
            describe_new=confdesc1, 
            product_list=conflist, 
            highlights=confhigh, 
            monthly_sales=confsale, 
            yearly_sales=confyear, 
            ebitda=confprofit, 
            physical_assets=confphy, 
            assets=confassets, 
            photos=chooseimage, 
            docs=choosedocs, 
            proof=choosefast)
        biz_obj.save()
        messages.success(
            request, " Your Business Profile succefully submitted")
        messages.success(
            request, " Profile is under verification")

    else:
        return HttpResponse("404 - Page Not Found")

    return redirect('/dashboard-status')


# Multi Step Form Submit Views Business
def bizform(request):
    return render(request, 'profile/businessform.html')


# def bizform_save(request):
#     if request.method != "POST":
#         return HttpResponseRedirect(reverse("multistepformexample"))
#     else:
#         fname = request.POST.get("fname")
#         lname = request.POST.get("lname")
#         phone = request.POST.get("phone")
#         twitter = request.POST.get("twitter")
#         facebook = request.POST.get("facebook")
#         gplus = request.POST.get("gplus")
#         email = request.POST.get("email")
#         password = request.POST.get("pass")
#         cpass = request.POST.get("cpass")
#         if password != cpass:
#             messages.error(request, "Confirm Password Doesn't Match")
#             return HttpResponseRedirect(reverse('business-profile'))

#         try:
#             multistepform = BizformModel(
#                 fname=fname, lname=lname, phone=phone, twitter=twitter, facebook=facebook, gplus=gplus, email=email, password=password)
#             multistepform.save()
#             messages.success(request, "Data Save Successfully")
#             return redirect('/dashboard-status')
#         except:
#             messages.error(request, "Error in Saving Data")
#             return HttpResponseRedirect(reverse('business-profile'))
# Multi step Form ends here


# Multi Step Form Submit Views Business
def investform(request):
    return render(request, 'profile/investform.html')


def investform_save(request):
    if request.method == "POST":
        # Get the post parameters
        iname = request.POST.get('iname')
        iemail = request.POST.get('iemail')
        iphone = request.POST.get('iphone')
        iprof = request.POST.get('iprof')
        iinterest = request.POST.get('iinterest')
        ifind = request.POST.get('ifind')
        iloc = request.POST.get('iloc')
        iprice = request.POST.get('iprice')
        icloc = request.POST.get('icloc')
        icomp = request.POST.get('icomp')
        idesg = request.POST.get('idesg')
        ilink = request.POST.get('ilink')
        ilink2 = request.POST.get('ilink2')
        ifactors = request.POST.get('ifactors')
        iassets = request.POST.get('iassets')
        isec = request.POST.get('isec')
        chooseiimage = request.POST.get('chooseiimage')
        chooseprofile = request.POST.get('chooseprofile')
        chooseterms = request.POST.get('chooseterms')
        chooseproof = request.POST.get('chooseproof')
        invest_obj = InvestmentProfile.objects.create(
            investor_name=iname, investor_mobile_number=iphone, investor_email=iemail, investor_profession=iprof, investor_interested_in=iinterest, investor_industry=ifind, investor_select_location=iloc, investor_investment_range=iprice, investor_current_location=icloc, investor_company=icomp, investor_designation=idesg, investor_companylink_1=ilink, investor_companylink_2=ilink2, investor_company_sector=isec, investor_factors=ifactors, investor_about_company=iassets, investor_logo=chooseiimage, investor_photos=chooseprofile, investor_docs=chooseterms, investor_proof=chooseproof,)
        invest_obj.save()
        messages.success(
            request, " Your Business Profile succefully submitted")
        messages.success(
            request, " Profile is under verification")

    else:
        return HttpResponse("404 - Page Not Found")

    return redirect('/dashboard-status')
