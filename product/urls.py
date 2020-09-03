from django.shortcuts import render
from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='product_home'),
    path('<category>/', views.product_category, name='product_category'),
    path('<category>/<int:pk>/', views.product_detail, name='product_detail'),

    path('new/', views.new, name='product_new'),
]
