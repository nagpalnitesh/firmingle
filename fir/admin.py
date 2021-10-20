from django.contrib import admin

# Register your models here.

from .models import User, Test

admin.site.register(User)

admin.site.register(Test)
