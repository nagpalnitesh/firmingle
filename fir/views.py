# from django.shortcuts import render
from django.views.generic import TemplateView


class Home(TemplateView):  # homePage requests
    template_name = 'index.html'  # Home Template


class About(TemplateView):  # AboutUs requests
    template_name = 'aboutus.html'  # About Us Template

    # return render(request, 'index.html')  # render index.html from templates
