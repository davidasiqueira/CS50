from django import views
from django.urls import URLPattern
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.great, name="great"),
    
    

]