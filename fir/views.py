# from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView

from .models import *


class Home(ListView):  # homePage requests
    model = Test
    template_name = 'index.html'  # Home Template


class About(TemplateView):  # AboutUs requests
    template_name = 'aboutus.html'  # About Us Template

    # return render(request, 'index.html')  # render index.html from templates
