from django.db import models
from empauth.models import Employee
from django.utils import timezone

# Create your models here.


class RoomStatus(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=1024)


class BookingCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField("Category Name", max_length=1024)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_no = models.IntegerField()
    room_type = models.CharField(max_length=1024)
    room_status = models.ForeignKey(RoomStatus, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(default=timezone.now())


class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # primary key is required by Django
    category = models.ForeignKey(
        BookingCategory, on_delete=models.DO_NOTHING, related_name="booking_category"
    )
    created_by = models.ForeignKey(
        Employee, on_delete=models.DO_NOTHING, related_name="booking_emp"
    )
    created_on = models.DateTimeField(default=timezone.now())
    updated_on = models.DateTimeField(auto_now_add=True)


class OPDBooking(models.Model):
    id = models.AutoField(primary_key=True)  # primary key is required by Django
    category = models.ForeignKey(
        BookingCategory,
        on_delete=models.DO_NOTHING,
        related_name="opd_booking_category",
    )
    created_by = models.ForeignKey(
        Employee, on_delete=models.DO_NOTHING, related_name="opd_booking_emp"
    )
    created_on = models.DateTimeField(default=timezone.now())
    updated_on = models.DateTimeField(auto_now_add=True)


class IPDBooking(models.Model):
    id = models.AutoField(primary_key=True)  # primary key is required by Django
    category = models.ForeignKey(
        BookingCategory,
        on_delete=models.DO_NOTHING,
        related_name="ipd_booking_category",
    )
    created_by = models.ForeignKey(
        Employee, on_delete=models.DO_NOTHING, related_name="ipd_booking_emp"
    )
    created_on = models.DateTimeField(default=timezone.now())
    updated_on = models.DateTimeField(auto_now_add=True)
