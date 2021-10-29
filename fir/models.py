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


class BusinessProfile(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    company = models.CharField(max_length=100, blank=True, default='')
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(
        validators=[phone_regex], max_length=15, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='')
    display_contact = models.CharField(max_length=100, blank=True, default='')
    display_company = models.CharField(max_length=100, blank=True, default='')
    plan_selected = models.CharField(max_length=50, blank=True, default='')
    is_accepted = models.BooleanField(default=False)
    profession = models.CharField(max_length=100, blank=True, default='')
    business_established = models.CharField(
        max_length=4, blank=True, default='')
    business_location = models.CharField(max_length=50, blank=True, default='')
    interested_in = models.CharField(max_length=50, blank=True, default='')
    industry = models.CharField(max_length=100, blank=True, default='')
    no_employees = models.PositiveBigIntegerField(default=0, blank=True)
    legal = models.CharField(max_length=100, blank=True, default='')
    describe = models.TextField(default='')
    describe_new = models.TextField(default='')
    highlights = models.TextField(default='')
    product_list = models.TextField(default='')
    facility = models.TextField(default='')
    monthly_sales = models.PositiveBigIntegerField(default=0, blank=True)
    yearly_sales = models.PositiveBigIntegerField(default=0, blank=True)
    ebitda = models.CharField(max_length=5, blank=True, default='')
    assets = models.TextField(default='')
    physical_assets = models.TextField(default='')
    photos = models.FileField(upload_to='photoimg', blank=False)
    docs = models.FileField(upload_to='doc', blank=False)
    proof = models.FileField(upload_to='proof_docs', blank=False)

    def __str__(self):
        return self.name
