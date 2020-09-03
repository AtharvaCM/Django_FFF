from django.shortcuts import render
from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.index, name='product_home'),
    path('<category>/', views.product_category, name='product_category'),
    path('<category>/<int:pk>/', views.product_detail, name='product_detail'),

    path('new/', views.new, name='product_new'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('/cart/cart-detail/', views.cart_detail, name='cart_detail'),
]
