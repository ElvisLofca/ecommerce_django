from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from core.permissions import IsOwner


class ReviewList(APIView):
    """
    Create a new review.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(APIView):
    """
    Retrieve, update or delete a reviews instance.
    """
    permission_classes = [IsOwner]

    def get_object(self, id):
        try:
            return Review.objects.get(id=id)
        except Review.DoesNotExist:
            raise Http404

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