from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BLANK_CHOICE_DASH
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
    name = models.CharField(max_length=50, null=True, blank=True, default='')
    company = models.CharField(
        max_length=100, null=True, blank=True, default='')
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(
        max_length=15, null=True, blank=True, default='')
    email = models.CharField(max_length=100, null=True, blank=True, default='')
    display_contact = models.CharField(
        max_length=100, null=True, blank=True, default='')
    display_company = models.CharField(
        max_length=100, null=True, blank=True, default='')
    plan_selected = models.CharField(
        max_length=50, null=True, blank=True, default='')
    is_accepted = models.BooleanField(default=False, null=True, blank=True)
    profession = models.CharField(
        max_length=100, null=True, blank=True, default='')
    business_established = models.CharField(
        max_length=4, null=True, blank=True, default='')
    business_location = models.CharField(
        max_length=50, null=True, blank=True, default='')
    interested_in = models.CharField(
        max_length=50, null=True, blank=True, default='')
    industry = models.CharField(
        max_length=100, null=True, blank=True, default='')
    no_employees = models.PositiveBigIntegerField(
        default=0, blank=True, null=True)
    legal = models.CharField(max_length=100, null=True, blank=True, default='')
    describe = models.TextField(null=True, blank=True, default='')
    describe_new = models.TextField(null=True, blank=True, default='')
    highlights = models.TextField(null=True, blank=True, default='')
    product_list = models.TextField(null=True, blank=True, default='')
    facility = models.TextField(null=True, blank=True, default='')
    monthly_sales = models.PositiveBigIntegerField(
        default=0, blank=True, null=True)
    yearly_sales = models.PositiveBigIntegerField(
        default=0, blank=True, null=True)
    ebitda = models.CharField(max_length=5, null=True, blank=True, default='')
    assets = models.TextField(null=True, blank=True, default='')
    physical_assets = models.TextField(default='', blank=True, null=True)
    photos = models.FileField(upload_to='photoimg', blank=True, null=True)
    docs = models.FileField(upload_to='doc', blank=True, null=True)
    proof = models.FileField(upload_to='proof_docs', blank=True, null=True)
    Status = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]
    profile_status = models.CharField(
        max_length=10, choices=Status, default='Pending')

    def __str__(self):
        return self.name


class InvestmentProfile(models.Model):
    investor_name = models.CharField(
        max_length=50, null=True, blank=True, default='')
    investor_mobile_number = models.CharField(
        max_length=15, null=True, blank=True, default='')
    investor_email = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_profession = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_interested_in = models.CharField(
        max_length=50, null=True, blank=True, default='')
    investor_industry = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_select_location = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_investment_range = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_current_location = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_company = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_designation = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_companylink_1 = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_companylink_2 = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_company_sector = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_factors = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_about_company = models.CharField(
        max_length=100, null=True, blank=True, default='')
    investor_logo = models.FileField(
        upload_to='companylogo', blank=True, null=True)
    investor_photos = models.FileField(
        upload_to='photoimg', blank=True, null=True)
    investor_docs = models.FileField(upload_to='doc', blank=True, null=True)
    investor_proof = models.FileField(
        upload_to='proof_docs', blank=True, null=True)
    Status = [
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    ]
    profile_status = models.CharField(
        max_length=10, choices=Status, default='Pending')

    def __str__(self):
        return self.investor_name
