from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH
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
    name = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=100, null=True)
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(max_length=15, null=True, blank=True),
    email = models.CharField(max_length=100, null=True)
    display_contact = models.CharField(
        max_length=100, null=True)
    display_company = models.CharField(
        max_length=100, null=True)
    plan_selected = models.CharField(max_length=50, null=True)
    is_accepted = models.BooleanField(default=False)
    profession = models.CharField(max_length=100, null=True)
    business_established = models.CharField(
        max_length=4, default='')
    business_location = models.CharField(
        max_length=50, null=True)
    interested_in = models.CharField(max_length=50, null=True)
    industry = models.CharField(max_length=100, null=True)
    no_employees = models.PositiveBigIntegerField(default=0)
    legal = models.CharField(max_length=100, null=True)
    describe = models.TextField(null=True)
    describe_new = models.TextField(null=True)
    highlights = models.TextField(null=True)
    product_list = models.TextField(null=True)
    facility = models.TextField(null=True)
    monthly_sales = models.PositiveBigIntegerField(default=0)
    yearly_sales = models.PositiveBigIntegerField(default=0)
    ebitda = models.CharField(max_length=5, null=True)
    assets = models.TextField(null=True)
    physical_assets = models.TextField(default='')
    photos = models.FileField(upload_to='photoimg')
    docs = models.FileField(upload_to='doc')
    proof = models.FileField(upload_to='proof_docs')

    def __str__(self):
        return self.name
