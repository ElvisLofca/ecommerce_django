from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsOwnerOrReadOnly, IsOwner
from orders.models import Order
from orders.serializers import OrderSerializer
from products.models import Product
from products.serializers import ProductSerializer
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from users.serializers import UserSerializer


class AdminUserList(APIView):
    """
    List all users, or create a new user.
    """
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class AdminUserDetail(APIView):
    """
    Retrieve, update or delete a users instance.
    """
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, id):
        users = self.get_object(id)
        serializer = UserSerializer(users)
        return Response(serializer.data)

    def put(self, request, id):
        users = self.get_object(id)
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        users = self.get_object(id)
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminProductList(APIView):
    """
        List all products, or create a new product.
    """
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminProductDetail(APIView):
    """
    Retrieve, update or delete a products instance.
    """
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, id):
        products = self.get_object(id)
        serializer = ProductSerializer(products)
        return Response(serializer.data)

    def put(self, request, id):
        products = self.get_object(id)
        serializer = ProductSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        products = self.get_object(id)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminReviewList(APIView):
    """
    List all reviews, or create a new review.
    """
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminReviewDetail(APIView):
    """
    Retrieve, update or delete a reviews instance.
    """
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, id):
        try:
            return Review.objects.get(id=id)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, id):
        reviews = self.get_object(id)
        serializer = ReviewSerializer(reviews)
        return Response(serializer.data)

    def put(self, request, id):
        reviews = self.get_object(id)
        serializer = ReviewSerializer(reviews, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        reviews = self.get_object(id)
        reviews.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminOrderList(APIView):
    """
    List all orders, or create a new order.
    """
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminOrderDetail(APIView):
    """
    Retrieve, update or delete an orders instance.
    """
    permission_classes = [permissions.IsAdminUser]

    def get_object(self, id):
        try:
            return Order.objects.get(id=id)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, id):
        orders = self.get_object(id)
        serializer = OrderSerializer(orders)
        return Response(serializer.data)

    def put(self, request, id):
        orders = self.get_object(id)
        serializer = OrderSerializer(orders, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        orders = self.get_object(id)
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
