from django import views
from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path("", views.isitnewyear, name="isitnewyear"),

]