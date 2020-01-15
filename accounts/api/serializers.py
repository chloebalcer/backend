from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import User
from django.shortcuts import get_object_or_404
User._meta.get_field('email')._unique = True
User._meta.get_field('username')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'status', 'student_code')
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password', 'status', 'student_code')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            status=validated_data['status'],
            student_code=validated_data['student_code'],
        )
        return user


def validateEmail(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


class LoginSerializer(serializers.Serializer):
    password = serializers.CharField()
    username = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # Check if user sent email
            if validateEmail(username):
                user_request = get_object_or_404(
                    User,
                    email=username,
                )
                username = user_request.username

        user = authenticate(username=username, password=password)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credential")

