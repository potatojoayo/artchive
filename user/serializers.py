from django.contrib.auth import authenticate, hashers
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):

        user = authenticate(email=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}


class RegisterSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):

        fields = ['email', 'password', 'name', 'nickname']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        password = validated_data.pop('password')
        hashed_pwd = hashers.make_password(password)
        user = User.objects.create(password=hashed_pwd, **validated_data)
        return user
