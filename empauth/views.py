from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import api_view
from rest_framework import status
import uuid


from .decorators import authenticate_user

# Create your views here.


@api_view(["GET"])
def get_all_emp(self, request):
    try:
        emps = Employee.objecs.all()
        serializer = EmployeeSerializer(emps)
        return JsonResponse(serializer.data, safe=False, status=200)

    except Exception as e:
        print(e)
        return JsonResponse({"error_msg": "Failed to fetch employess"}, status=401)


@api_view(["POST"])
def emp_create(request):
    try:
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            # Hash the password before saving
            hashed_password = make_password(request.data.get("password"))
            print(hashed_password)
            serializer.save(password=hashed_password)
            return JsonResponse(
                {"Success_msg": "Employee created."}, status=status.HTTP_201_CREATED
            )
        else:
            return JsonResponse(
                {"error_msg": "Incorrect Data"}, status=status.HTTP_400_BAD_REQUEST
            )

    except Exception as e:
        print(e)
        return Response(
            {"error_msg": "Employee creation failed."},
            status=status.HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
def emplogin(request):
    username = request.data.get("username")
    password = request.data.get("password")

    print(username, password)

    # Find the employee by username
    try:
        employee = Employee.objects.get(username=username)
    except Employee.DoesNotExist:
        return JsonResponse(
            {"message": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED
        )

    # Check the entered password against the stored hashed password
    if employee is not None and check_password(password, employee.password):
        token_value = uuid.uuid4()
        try:
            employee_token = EmployeeToken.objects.create(
                employee=employee, token=token_value
            )
        except Exception as e:
            print(e)
            return JsonResponse(
                {"message": "Login failed"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return JsonResponse(
            {"token": str(token_value), "message": "Login successful"},
            status=status.HTTP_200_OK,
        )

    return JsonResponse(
        {"message": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED
    )
