from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from products.models import Product

import logging
logger = logging.getLogger(__name__)


class TestAdminProductViews(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Defining urls
        self.admin_products_url = reverse('admin-products')
        # self.admin_product_detail_url = reverse('admin-product-detail')

        # Defining users
        self.superuser = User.objects.create_superuser(username='admin', email='admin@mail.com', password='admin')
        self.authenticated_user = User.objects.create_user(username='member', email='member@mail.com', password='member')

        # Defining product and data
        self.product_data = {'user': self.superuser.id, 'name': 'Item name 1', 'description': 'Item description 1', 'price': 200.00, 'count_in_stock': 1, 'rating': 1}
        Product.objects.create(user=self.superuser, name='Item name 2', description='Item description 2', price=200.00, count_in_stock=1, rating=1)

        # Authenticating with superuser
        self.client.force_authenticate(user=self.superuser)

    def test_list_products(self):
        response = self.client.get(self.admin_products_url)
        self.assertEquals(response.status_code, 200)

    def test_create_product(self):
        response = self.client.post(self.admin_products_url, data=self.product_data)
        data = response.data

        self.assertEquals(data['name'], self.product_data['name'])
        self.assertEquals(data['description'], self.product_data['description'])
        self.assertEquals(float(data['price']), self.product_data['price'])
        self.assertEquals(data['count_in_stock'], self.product_data['count_in_stock'])
        self.assertEquals(float(data['rating']), self.product_data['rating'])
        self.assertEquals(response.status_code, 201)

    # def test_get_product(self):
    #     response = self.client.get(self.detail_url)
    #     self.assertEquals(response.status_code, 200)
    #
    # def test_update_product(self):
    #     response = self.client.put(self.detail_url, self.dummy_update)
    #     # Check why 415
    #     self.assertEquals(response.status_code, 415)
    #
    # def test_delete_product(self):
    #     response = self.client.delete(self.detail_url)
    #     self.assertEquals(response.status_code, 204)

    def test_list_products_with_authenticated_user(self):
        self.client.force_authenticate(user=self.authenticated_user)
        response = self.client.get(self.admin_products_url)
        self.assertEquals(response.status_code, 403)