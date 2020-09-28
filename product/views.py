from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import AddToCartForm
from cart.views import add_to_cart
from django.contrib import messages


# Create your views here.


def index(request):
    # List all categories
    categories = Category.objects.all()
    if categories is not None:
        return render(request, 'product/index.html', {'categories': categories})
    return render(request, 'product/index.html')


def product_category(request, category):
    # List all products in the resp category
    products = Product.objects.filter(categories__name__contains=category)
    context = {
        "category": category,
        "products": products
    }
    return render(request, "product/product_catagory.html", context)


def product_detail(request, category, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = AddToCartForm(request.POST, instance=product)
        if form.is_valid():
            msg = form.save(request=request, category=category,
                            product=product, quantity=form.cleaned_data.get('quantity'))
            print(msg)
            if msg == f'Item added in cart':
                flag = 1
            else:
                flag = 2
            context = {
                "product": product,
                "form": form,
                "msg": msg,
                "flag": flag
            }
            return render(request, "product/product_detail.html", context)
    else:
        form = AddToCartForm()
    context = {
        "product": product,
        "form": form,
        "msg": None,
        "flag": 0
    }
    return render(request, "product/product_detail.html", context)


def new(request):
    # This is not meant for the customers
    return HttpResponse("This is the new products section!")
