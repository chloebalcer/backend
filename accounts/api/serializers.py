from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.shortcuts import get_object_or_404
User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user

def validateEmail( email ):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

class LoginSerializer(serializers.Serializer):   
    # email = serializers.CharField()
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

        r = authenticate(username=username, password=password)

            
        user = authenticate(username=username,password=password)
        if user and user.is_active:
             return user
        raise serializers.ValidationError("Incorrect Credential")

