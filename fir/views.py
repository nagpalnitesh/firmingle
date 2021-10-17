from django.shortcuts import render

from django.http import HttpResponse


def home(request):  # homePage requests
    return HttpResponse('Hello World!')
