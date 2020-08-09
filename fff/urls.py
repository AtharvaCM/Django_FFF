from django.urls import path

from . import views

app_name = 'fff'

# this module contains the links on the landing page adn the overview of the app

urlpatterns = [
    path('', views.index, name='freshfromfarm-home'),
    path('about/', views.about, name='freshformfarm-about'),
    path('contact/', views.contact, name='freshfromfarm-contact'),
]
