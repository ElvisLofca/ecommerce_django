from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers import SignInTokenObtainPairSerializer, SignUpSerializer


import logging
logger = logging.getLogger(__name__)

class SignUpView(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInView(TokenObtainPairView):
    logger.info('testtest')
    logger.warning('testtest')
    logger.error('testtest')
    logger.critical('testtest')
    serializer_class = SignInTokenObtainPairSerializer