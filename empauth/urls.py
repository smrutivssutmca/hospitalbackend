from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.emplogin),
    path("create/", views.emp_create),
    path("/", views.get_all_emp),
]
