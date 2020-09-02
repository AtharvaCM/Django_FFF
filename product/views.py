from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def index(request):
    # List all categories
    categories = Category.objects.all()
    if categories is not None:
        return render(request, 'product/index.html', {'categories': categories})
    return render(request, 'product/index.html')


def product_category(request, category):
    # List all products in the resp categorys
    products = Product.objects.filter(categories__name__contains=category)
    context = {
        "category": category,
        "products": products
    }
    return render(request, "product/product_catagory.html", context)


def new(request):
    # This is not meant for the customers
    return HttpResponse("This is the new products section!")
