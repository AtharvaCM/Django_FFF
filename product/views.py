from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    if products is not None:
        return render(request, 'product/index.html', {'products': products})
    return render(request, 'product/index.html')


def new(request):
    return HttpResponse("This is the new products section!")
