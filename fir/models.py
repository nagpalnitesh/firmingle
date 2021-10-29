from django.db import models
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.core.validators import RegexValidator
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


class BusinessProfile(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=False)
    email = models.CharField(max_length=100)
    display_contact = models.CharField(max_length=100)
    display_company = models.CharField(max_length=100)
    plan_selected = models.CharField(max_length=50)
    is_accepted = models.BooleanField(default=False)
    profession = models.CharField(max_length=100)
    business_established = models.CharField(max_length=4)
    business_location = models.CharField(max_length=50)
    interested_in = models.CharField(max_length=50)
    industry = models.CharField(max_length=100)
    no_employees = models.PositiveBigIntegerField()
    legal = models.CharField(max_length=100)
    describe = models.TextField()
    describe_new = models.TextField()
    highlights = models.TextField()
    product_list = models.TextField()
    facility = models.TextField()
    monthly_sales = models.PositiveBigIntegerField()
    yearly_sales = models.PositiveBigIntegerField()
    ebitda = models.CharField(max_length=5)
    assets = models.TextField()
    physical_assets = models.TextField()
    photos = models.FileField(upload_to='photoimg', blank=False)
    docs = models.FileField(upload_to='doc', blank=False)
    proof = models.FileField(upload_to='proof_docs', blank=False)

    def __str__(self):
        return self.name
