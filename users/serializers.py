from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# Здесь нам придется переопределить сериалайзер, который использует djoser
# для создания пользователя из-за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        """ Перечислить все поля, которые могут быть включены в запрос
        или ответ, включая поля, явно указанные выше. """
        model = User
        fields = '__all__'

    def create(self, validated_data):
        """ Использовать метод create_user, который мы
        написали ранее, для создания нового пользователя. """
        return User.objects.create_user(**validated_data)


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        """ Перечислить все поля, которые могут быть включены в запрос
        или ответ, включая поля, явно указанные выше. """
        model = User
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone = validated_data.get("phone", instance.phone)
        instance.last_login = validated_data.get("last_login", instance.last_login)
        instance.image = validated_data.get("image_", instance.image)
        instance.save()
        return instance
