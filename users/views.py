from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions import IsOwner
from users.serializers import UserSerializer


class UserDetail(APIView):
    """
    Retrieve, update or delete a users instance.
    """
    permission_classes = [IsOwner]

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