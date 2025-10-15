from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated


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
