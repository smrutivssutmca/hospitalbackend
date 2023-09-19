from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status

from empauth.decorators import authenticate_user


@api_view(["GET"])
@authenticate_user
def get_all_bookings(request):
    try:
        bookings = Booking.objects.all()
        serializer = BookingSerializers(bookings, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    except Exception as e:
        print(e)
        return JsonResponse({"error_msg": "Failed to fetch bookings"}, status=401)


@api_view(["POST"])
@authenticate_user
def create_booking(request):
    try:
        serializer = BookingSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"Success_msg": "Booking created."}, status=status.HTTP_201_CREATED
            )
        else:
            return JsonResponse(
                {"error_msg": "Incorrect Data"}, status=status.HTTP_400_BAD_REQUEST
            )

    except Exception as e:
        print(e)
        return JsonResponse(
            {"error_msg": "Booking creation failed."},
            status=status.HTTP_400_BAD_REQUEST,
        )
