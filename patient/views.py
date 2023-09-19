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
def create_patient_user(request):
    try:
        serializer = PatientUserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"Success_msg": "Patient user created."}, status=status.HTTP_201_CREATED
            )
        else:
            return JsonResponse(
                {"error_msg": "Incorrect Data"}, status=status.HTTP_400_BAD_REQUEST
            )

    except Exception as e:
        print(e)
        return JsonResponse(
            {"error_msg": "Patient user creation failed."},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
@authenticate_user
def create_patient_details(request):
    try:
        serializer = PatientInfoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"Success_msg": "Patient details created."},
                status=status.HTTP_201_CREATED,
            )
        else:
            return JsonResponse(
                {"error_msg": "Incorrect Data"}, status=status.HTTP_400_BAD_REQUEST
            )

    except Exception as e:
        print(e)
        return JsonResponse(
            {"error_msg": "Patient details creation failed."},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
def get_single_patient_history(request, pk):
    try:
        patient = PatientInfo.objects.get(patient_id=pk)
        history = PatientHistory.objects.filter(patient=patient)
        serializer = PatientHistorySerializers(history, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    except Exception as e:
        print(e)
        return JsonResponse(
            {"error_msg": "Failed to fetch patient history"}, status=401
        )
