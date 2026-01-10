# Django e django rest
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Adiciona informações customizadas ao payload do token
        # (Opcional, mas útil para o lado do cliente)
        token['username'] = user.username
        token['email'] = user.email
        
        # Você pode adicionar grupos, permissões, etc.
        user_groups = [group.name for group in user.groups.all()]
        token['groups'] = user_groups 

        return token

    def validate(self, attrs):
        # Chama a função validate original para obter os tokens 'access' e 'refresh'
        data = super().validate(attrs)

        # Adiciona os dados do usuário à resposta (payload)
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
        }

        return data
    
class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )

        # Busca ou cria o grupo "user"
        group, created = Group.objects.get_or_create(name="user")

        # Adiciona o usuário ao grupo
        user.groups.add(group)

        return user