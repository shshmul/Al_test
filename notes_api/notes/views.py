from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# кастомный сериализатор для создания jwt-токена
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Создание стандартного токена (родительский метод)
        token = super().get_token(user)
        token['username'] = user.username
        return token

# кастомное представление для получения jwt-токена
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# получение списка и создания заметок
class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    # Только для пользователей которые прошли аутентификацию
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Только заметки текущего пользователя
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Создание новой заметки текущего пользователя
        serializer.save(user=self.request.user)

# получение, обновление и удаление заметок
class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    # Только для пользователей которые прошли аутентификацию
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Только заметки текущего пользователя
        return Note.objects.filter(user=self.request.user)

# регистрация пользователя
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # для всех доступ
    permission_classes = [permissions.AllowAny]

# обновление токена пользователя
class CustomTokenRefreshView(TokenRefreshView):
    pass
