from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Product
from products.serializers import ProductSerializer


class ProductList(APIView):
    """
    create a new product.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    """
    Retrieve a products instance.
    """
    permission_classes = [permissions.IsAdminUser, permissions.BasePermission]

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id):
        products = self.get_object(id)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
