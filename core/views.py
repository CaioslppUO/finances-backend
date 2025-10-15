from rest_framework import status
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from django.urls import reverse
from drf_yasg.utils import swagger_auto_schema


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
