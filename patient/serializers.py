from rest_framework import serializers
from .models import *


class PatientUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientUser
        fields = "__all__"


class PatientInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientInfo
        fields = "__all__"


class PatientHistorySerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientHistory
        fields = "__all__"
