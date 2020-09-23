from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from product import views as views


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('product:product_home')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.index)

    def test_product_category_url_is_resolved(self):
        url = reverse('product:product_category', args=['category'])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.product_category)

    def test_product_detail_url_is_resolved(self):
        url = reverse('product:product_detail', args=['category', '01'])
        # print(resolve(url))
        self.assertEquals(resolve(url).func, views.product_detail)

    # def test_new_product_url_is_resolved(self):
    #     url = reverse('product:product_new')
    #     # print(resolve(url))
    #     self.assertEquals(resolve(url).func, views.new)
