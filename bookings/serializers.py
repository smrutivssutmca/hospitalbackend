from rest_framework import serializers
from .models import *


class RoomStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomStatus
        fields = "__all__"


class BookingCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = BookingCategory
        fields = "__all__"


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class OPDBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = OPDBooking
        fields = "__all__"


class IPDBookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = IPDBooking
        fields = "__all__"
