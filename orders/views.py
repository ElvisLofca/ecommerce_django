from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from orders.models import Order
from core.permissions import IsOwnerOrReadOnly, IsOwner
from orders.serializers import OrderSerializer


class OrderList(APIView):
    """
    List all orders, or create a new order.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    """
    Retrieve, delete an orders instance.
    """
    permission_classes = [IsOwner]

    def get_object(self, id):
        try:
            return Order.objects.get(id=id)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, id):
        orders = self.get_object(id)
        serializer = OrderSerializer(orders)
        return Response(serializer.data)

    def delete(self, request, id):
        orders = self.get_object(id)
        orders.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)