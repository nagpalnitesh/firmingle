# Generated by Django 3.2.8 on 2021-10-29 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('company', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('phone', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('display_contact', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('display_company', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('plan_selected', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('is_accepted', models.BooleanField(blank=True, default=False, null=True)),
                ('profession', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('business_established', models.CharField(blank=True, default='', max_length=4, null=True)),
                ('business_location', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('interested_in', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('industry', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('no_employees', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('legal', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('describe', models.TextField(blank=True, default='', null=True)),
                ('describe_new', models.TextField(blank=True, default='', null=True)),
                ('highlights', models.TextField(blank=True, default='', null=True)),
                ('product_list', models.TextField(blank=True, default='', null=True)),
                ('facility', models.TextField(blank=True, default='', null=True)),
                ('monthly_sales', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('yearly_sales', models.PositiveBigIntegerField(blank=True, default=0, null=True)),
                ('ebitda', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('assets', models.TextField(blank=True, default='', null=True)),
                ('physical_assets', models.TextField(blank=True, default='', null=True)),
                ('photos', models.FileField(blank=True, null=True, upload_to='photoimg')),
                ('docs', models.FileField(blank=True, null=True, upload_to='doc')),
                ('proof', models.FileField(blank=True, null=True, upload_to='proof_docs')),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investor_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('investor_mobile_number', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('investor_email', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_profession', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_interested_in', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('investor_industry', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_select_location', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_investment_range', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_current_location', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_company', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_designation', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_companylink_1', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_companylink_2', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_company_sector', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_factors', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_about_company', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('investor_logo', models.FileField(blank=True, null=True, upload_to='companylogo')),
                ('investor_photos', models.FileField(blank=True, null=True, upload_to='photoimg')),
                ('investor_docs', models.FileField(blank=True, null=True, upload_to='doc')),
                ('investor_proof', models.FileField(blank=True, null=True, upload_to='proof_docs')),
            ],
        ),
    ]
