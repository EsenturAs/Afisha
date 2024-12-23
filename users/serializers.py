from rest_framework import serializers
from rest_framework.authtoken.admin import User
from rest_framework.exceptions import ValidationError


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise ValidationError('A user with that username already exists!')
