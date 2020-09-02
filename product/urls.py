from django.shortcuts import render
from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index),
    path('new/', views.new)
]