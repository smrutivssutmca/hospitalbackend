from django.db import models
from django.utils import timezone
import uuid

# Create your models here.


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField("Name", max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class EmployeeToken(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.token)
