from django.test import TestCase
from django.urls import reverse, resolve
from administration.views import AdminProductDetail, AdminProductList


class TestUrls(TestCase):

    def test_list_url_resolves(self):
        url = reverse('admin-products')
        self.assertEquals(resolve(url).func.view_class, AdminProductList)

    def test_detail_url_resolves(self):
        url = reverse('admin-product-detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, AdminProductDetail)