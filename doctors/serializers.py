from rest_framework import serializers
from .models import *


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"
