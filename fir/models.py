from django.db import models
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
# Create your models here.


# class Person(models.Model):
#     user_name = models.ForeignKey(
#         'auth.User',
#         on_delete=models.CASCADE,
#     )
#     Name = models.CharField(max_length=100)
#     Company = models.CharField(max_length=100)
#     Designation = models.CharField(max_length=100)
#     GST_Number = models.CharField(max_length=100)
#     Address = models.CharField(max_length=100)

#     def __str__(self):
#         return self.Name


# Login/ SignUp Token
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # authenication token
    auth_token = models.CharField(max_length=100)
    # check account is verified or not
    isVerified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # forget password token
    forget_password_token = models.CharField(max_length=100)

    def __str__(self):
        return self.user.first_name


class UserProfile(DetailView):
    model = Profile
    models.SlugField(("username"))
    template_name = 'fir/dashboard.html'
