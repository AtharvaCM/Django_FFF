from django.shortcuts import render, reverse
from cart.models import Cart

# Create your views here.


def view_cart(request):
    template_name = 'cart/view_cart.html'
    context = {}

    if request.user.is_authenticated:
        items = Cart.objects.filter(user=request.user)
        print(items)
        context = {
            'items': items,
        }

    return render(request, template_name, context)


def add_to_cart(request, category, product, qty):
    user = request.user
    try:
        Cart.objects.create(user=user, product=product, quantity=qty)
    except:
        return f'Item already present in cart'
    print(category)
    print(product.pk)

    # return reverse('product:product_detail', args=['category', 'product.pk'])
    return f'Item added in cart'
