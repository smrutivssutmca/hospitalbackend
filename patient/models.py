from django.db import models
from bookings.models import *
from doctors.models import *
from empauth.models import Employee

# Create your models here.


class PatientUser(models.Model):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=100)
    created_by = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    is_removed = models.BooleanField(default=False)


class PatientInfo(models.Model):
    id = models.AutoField(primary_key=True)
    patient_user = models.ForeignKey(PatientUser, on_delete=models.DO_NOTHING)
    patient_id = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    patient_age = models.IntegerField()
    patient_dob = models.DateField()
    mobile = models.CharField(max_length=100)
    alt_mobile = models.CharField(max_length=100)
    address = models.TextField()
    father_name = models.CharField(max_length=100)
    patient_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    is_removed = models.BooleanField(default=False)


class PatientHistory(models.Model):
    id = models.AutoField(primary_key=True)
    patient_info = models.ForeignKey(PatientInfo, on_delete=models.DO_NOTHING)
    romm_no = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    dcotor_attened = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING)
    pre_illness = models.TextField(null=True, blank=True)
    disease = models.TextField(null=True, blank=True)
    discussion = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)
    discharge_date = models.DateField()
    disablity = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_removed = models.BooleanField(default=False)
