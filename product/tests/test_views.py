from django.test import TestCase, Client
from django.urls import reverse
from product.models import Product, Category
import json


class TestViews(TestCase):

    def setUp(self):
        self.category1 = Category.objects.create(name='category1')
        self.product1 = Product.objects.create(
            title='product1', price=10)
        # self.product1.categories.add(self.category1.id)

        self.client = Client()
        self.index_url = reverse('product:product_home')
        self.product_category_url = reverse(
            'product:product_category', args=['category1'])
        self.product_detail_url = reverse(
            'product:product_detail', args=['category1', '3'])
        # product_detail_GET faisl coz the setUp gets called 3 times and the product id became 3
        # so either use separate setup or pass the corect id

    def test_category_list_GET(self):
        # test
        response = self.client.get(self.index_url)
        # assert
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/index.html')

    def test_product_category_list_GET(self):
        # test
        response = self.client.get(self.product_category_url)
        # assert
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_catagory.html')

    def test_product_detail_GET(self):
        # test
        response = self.client.get(self.product_detail_url)
        # assert
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/product_detail.html')
