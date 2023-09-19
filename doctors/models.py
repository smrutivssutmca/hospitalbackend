from django.db import models
from empauth.models import Employee


# Create your models here.


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024)


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024)
    department = models.ForeignKey("Department", on_delete=models.DO_NOTHING)
    mobile = models.CharField(max_length=1024)
    alt_mobile = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024)
    address = models.TextField()
    created_by = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
