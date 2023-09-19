# decorators.py
import jwt
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from .models import *


def authenticate_user(view_func):
    def _wrapped_view(request, *args, **kwargs):
        token = request.META.get(
            "HTTP_AUTHORIZATION"
        )  # Assuming the token is sent in the 'Authorization' header
        if not token:
            return Response(
                {"message": "Authentication credentials not provided"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return Response(
                {"message": "Token has expired"}, status=status.HTTP_401_UNAUTHORIZED
            )
        except jwt.DecodeError:
            return Response(
                {"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
            )

        # check the user id exists or not
        try:
            emp_user_model = Employee.objects.get(id=payload.get("id"))
        except Exception as e:
            return Response(
                {"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
            )

        # Store the user ID in the request for access in the view
        if emp_user_model:
            request.user_id = payload.get("id")
        else:
            return Response(
                {"message": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED
            )
        return view_func(request, *args, **kwargs)

    return _wrapped_view
