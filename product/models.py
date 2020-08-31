from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    stock = models.IntegerField(default='0')
    image_src = models.CharField(max_length=2083, blank=True)

    # dynamic urls
    def get_absolute_url(self):
        # f"/products/{self.id}/"
        return reverse("products:product-detail", kwargs={"id": self.id})
