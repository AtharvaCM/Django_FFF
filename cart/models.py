from django.db import models
from django.db.models import CheckConstraint, Q
from django.contrib.auth.models import User
from product.models import Product
from django.core.exceptions import ValidationError

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = (('user', 'product'),)
        constraints = [
            CheckConstraint(
                check=Q(quantity__gt=0), name='check_quantity_value',
            ),
        ]

    def clean(self):
        if self.quantity <= 0:
            # raise ValueError('Quantity cannot be zero or negative')
            raise ValidationError('Quantity cannot be zero or negatives')

    def __str__(self):
        return str(self.user)
