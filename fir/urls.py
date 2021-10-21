"""fir App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # indexPage
    # path('', views.home, name="home"),
    # path('about/', views.About.as_view(), name='about_us'),  # aboutPage
    path('signup/', views.signup, name='signup'),  # signupPage
    path('login/', views.login, name='login'),  # loginPage
    # path('logout/', views.logout, name='logout'),  # logoutPage
    # path('invited_user/', views.invited_user, name='newuser'),
    # url('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
    #     views.activate_account, name='activate'),
    path('token/', views.token_send, name='token_send'),  # token_sendPage
    path('success/', views.success, name='success'),  # successPage
    path('verify/<auth_token>', views.verify, name='verify'),  # verifyPage
    path('error/', views.error, name='error'),  # errorPage
    path('forget-password/', views.forget_password,
         name='forget_password'),  # forget_passwordPage
    path('reset-password/<token>',
         views.change_password, name="reset password")
]
