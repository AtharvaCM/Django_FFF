from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    image_src = models.CharField(max_length=2083, blank=True)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    stock = models.IntegerField(default='0')
    categories = models.ManyToManyField('Category', related_name='products')
    image_src = models.CharField(max_length=2083, blank=True)

    def __str__(self):
        return str(self.title)

    # dynamic urls
    def get_absolute_url(self):
        # f"/products/{self.id}/"
        return reverse("products:product-detail", kwargs={"id": self.id})
