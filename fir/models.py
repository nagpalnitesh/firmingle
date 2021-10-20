from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Test(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Person(models.Model):
    Name = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    Company = models.TextField()
    Designation = models.CharField(max_length=100)
    GST_Number = models.TextField()
    Address = models.TextField()

    def __str__(self):
        return self.Name
