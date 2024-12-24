from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics, views
from django.contrib.auth.models import User
from . import serializers, models
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from random import randint


class RegistrationAPIView(views.APIView):
    def post(self, request):
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(username=username, password=password, is_active=False)

        secret_code = randint(100000, 999999)
        models.UserConfirmation.objects.create(user=user, secret_code=secret_code)

        return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)


class ConfirmationAPIView(views.APIView):
    def post(self, request):
        user = request.data.get('user')
        secret_code = request.data.get('secret_code')
        try:
            confirm = models.UserConfirmation.objects.get(user=user, secret_code=secret_code)
            user = User.objects.get(id=confirm.user.id)
            user.is_active = True
            user.save()
            return Response(data={'user_id': user.id}, status=status.HTTP_200_OK)
        except:
            return Response(data={'user_id': user.id}, status=status.HTTP_400_BAD_REQUEST)


class AuthorizationAPIView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)
            return Response(data={'token': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def registration_api_view(request):
#     serializer = serializers.UserRegistrationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     username = serializer.validated_data.get('username')
#     password = serializer.validated_data.get('password')
#
#     user = User.objects.create_user(username=username, password=password, is_active=False)
#     secret_code = randint(100000, 999999)
#     models.UserConfirmation.objects.create(user=user, secret_code=secret_code)
#
#     return Response(data={'user_id': user.id}, status=status.HTTP_201_CREATED)


# @api_view(['POST'])
# def confirmation_api_view(request):
#     user = request.data.get('user')
#     secret_code = request.data.get('secret_code')
#     try:
#         confirm = models.UserConfirmation.objects.get(user=user, secret_code=secret_code)
#         user = User.objects.get(id=confirm.user.id)
#         user.is_active = True
#         user.save()
#         return Response(data={'user_id': user.id}, status=status.HTTP_200_OK)
#     except:
#         return Response(data={'user_id': user.id}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def authorization_api_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#
#     user = authenticate(username=username, password=password)
#     if user:
#
#         token = Token.objects.get_or_create(user=user)
#         return Response(data={'token': token.key})
#     return Response(status=status.HTTP_401_UNAUTHORIZED)
