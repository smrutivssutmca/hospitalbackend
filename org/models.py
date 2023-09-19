from django.db import models

# Create your models here.


class Organisation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024)
    mobile = models.CharField(max_length=1024)
    address = models.TextField()
    pincode = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    registration_number = models.CharField(max_length=1024)
    logo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
