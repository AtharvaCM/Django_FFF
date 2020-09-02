from django.shortcuts import render
from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='product_home'),
    path('new/', views.new, name='produc_tnew'),
    path("<category>/", views.product_category, name="product_category"),
]
