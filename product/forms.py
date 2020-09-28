from django import forms
from cart.models import Cart
from cart.views import add_to_cart
from django.core.exceptions import ValidationError

from django.forms.utils import ErrorList


class DivErrorList(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error alert alert-danger mt-1">%s</div>' % e for e in self])


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']

    def clean_quantity(self):
        data = self.cleaned_data['quantity']
        if data <= 0:
            raise ValidationError('Invalid quantity bro!')
        return data

    def save(self, request, category, product, quantity, commit=True, *args, **kwargs):
        msg = add_to_cart(request, category=category,
                          product=product, qty=quantity)
        return msg
