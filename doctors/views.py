from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework import status

from empauth.decorators import authenticate_user


@api_view(["POST"])
@authenticate_user
def create_doctor(request):
    try:
        serializer = DoctorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"Success_msg": "Doctor created."}, status=status.HTTP_201_CREATED
            )
        else:
            return JsonResponse(
                {"error_msg": "Incorrect Data"}, status=status.HTTP_400_BAD_REQUEST
            )

    except Exception as e:
        print(e)
        return JsonResponse(
            {"error_msg": "Doctor creation failed."},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def get_all_doctors(request):
    try:
        doctors = Doctor.objects.all()
        serializer = DoctorSerializers(doctors, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    except Exception as e:
        print(e)
        return JsonResponse({"error_msg": "Failed to fetch doctors"}, status=401)


@api_view(["GET"])
def get_departments(request):
    try:
        departments = Department.objects.all()
        serializer = DepartmentSerializers(departments, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    except Exception as e:
        print(e)
        return JsonResponse({"error_msg": "Failed to fetch departments"}, status=401)
