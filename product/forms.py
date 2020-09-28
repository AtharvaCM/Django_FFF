from django import forms
from cart.models import Cart
from cart.views import add_to_cart


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']

    def save(self, request, category, product, quantity, commit=True, *args, **kwargs):
        msg = add_to_cart(request, category=category,
                          product=product, qty=quantity)
        return msg
