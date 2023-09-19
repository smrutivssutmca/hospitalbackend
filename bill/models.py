from django.db import models
from patient.models import *
from bookings.models import *

# Create your models here.


class PaymentMode(models.Model):
    id = models.AutoField(primary_key=True)
    payment_mode = models.CharField(max_length=100)
    is_removed = models.BooleanField(default=False)


class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    patient_info = models.ForeignKey(PatientInfo, on_delete=models.DO_NOTHING)
    Booking = models.ForeignKey(Booking, on_delete=models.DO_NOTHING)
    invoice_no = models.CharField(max_length=100)
    invoice_date = models.DateField()
    total_amount = models.FloatField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_removed = models.BooleanField(default=False)


class PaymentDetails(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING)
    payment_date = models.DateField()
    payment_mode = models.CharField(max_length=100)
    paid_amount = models.FloatField()
    balance_amount = models.FloatField()
    payment_mode = models.ForeignKey(PaymentMode, on_delete=models.DO_NOTHING)
    check_no = models.CharField(max_length=100, null=True, blank=True)
    check_date = models.CharField(max_length=100, null=True, blank=True)
    bank_name = models.CharField(max_length=100, null=True, blank=True)
    branch_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_removed = models.BooleanField(default=False)
