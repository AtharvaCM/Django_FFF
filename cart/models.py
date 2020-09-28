from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)

    class Meta:
        unique_together = (('user', 'product'),)

    def __str__(self):
        return str(self.user)
