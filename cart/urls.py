from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view-cart'),
    path('add/<category>/<product>/<int>',
         views.add_to_cart, name='add-to-cart'),
]
