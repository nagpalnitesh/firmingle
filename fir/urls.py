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
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # indexPage
    path('privacy', views.privacy, name='privacy'),  # privacyPage
    path('terms-and-condition', views.terms, name='terms'),  # termsPage
    path('faq', views.faq, name='faq'),  # faqPage
    path('signup', views.signup, name='signup'),  # signupPage
    path('login', views.handlelogin, name='login'),  # loginPage
    path('logout', views.handlelogout, name='logout'),  # logoutPage
    path('verify/<auth_token>', views.verify, name='verify'),  # verifyPage
    path('error/', views.error, name='error'),  # errorPage
    path('forget-password', views.forget_password,
         name='forget_password'),  # forget_passwordPage
    path('reset-password/<token>', views.change_password,
         name="reset password"),  # reset_passwordPage
    path('press', views.press, name='press'),  # pressPage
    path('aboutus', views.about, name='aboutus'),  # aboutusPage
    path('contactus', views.contact, name='contactus'),  # contactusPage
    path('dashboard', views.dashboard,
         name='dashboard'),  # dashboardPage
    path('dashboard-status', views.dashboard_status,
         name='dashboard'),  # dashboardPage
    path('investors-and-buyers', views.browseInvestor,
         name="Investors"),  # Browse Investors
    path('business-for-sale-and-investment-opportunities',
         views.browseBusiness, name="Business"),  # Browse Business
    path('detail-profile', views.detailPost, name="detail"),  # detailPost
    path('businessadd', views.businessAdd, name="businessAdd"),  # businessadd




    path('business-profile', views.bizform, name="bizform"),  # businessadd
    # path('bizform_save', views.bizform_save,
    #    name="bizform_save"),  # businessadd

    path('investor-profile', views.investform, name="investform"),  # investadd
    path('investform_save', views.investform_save,
         name="investform_save"),  # investadd
]
