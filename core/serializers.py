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