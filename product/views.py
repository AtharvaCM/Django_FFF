from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Category
from .forms import QtyForm
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


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
    form = QtyForm()
    if request.method == 'POST':
        form = QtyForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        "product": product,
        "form": form,
    }
    return render(request, "product/product_detail.html", context)


def new(request):
    # This is not meant for the customers
    return HttpResponse("This is the new products section!")


@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('product:product_home')


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_detail(request):
    return render(request, 'product/cart_detail.html')
