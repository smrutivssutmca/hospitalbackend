from rest_framework import serializers
from .models import *


class PaymentModeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaymentMode
        fields = "__all__"


class InvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = "__all__"


class PaymentDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = "__all__"
