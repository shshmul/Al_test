from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        # extra_kwargs = {'password': {'write_only': True}}
    # Создание пользователя
    def create(self, validated_data):
        user =  User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

# Управление заметками (структура представления)
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')