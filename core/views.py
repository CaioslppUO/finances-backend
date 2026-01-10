from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(auto_schema=None)
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("swagger-ui"))

    @swagger_auto_schema(auto_schema=None)
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(reverse("swagger-ui"))

class CustomTokenObtainPairView(TokenObtainPairView):
    # Usa o Serializer customizado
    serializer_class = CustomTokenObtainPairSerializer

class UserCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer