"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Django
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, reverse
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenRefreshView

# Yasg
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Schemas
schema_view = get_schema_view(
    openapi.Info(
        title="Expenses API",
        default_version="v1",
        description="API to manage monthly expenses.",
    ),
    public=True,
    authentication_classes=[],
    permission_classes=[AllowAny],
)

# Views
from .views import LogoutView
from .views import UserCreateView
from .views import CustomTokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("expenses.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/accounts/logout/", LogoutView.as_view(), name="logout"),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path(
        "accounts/logout/",
        lambda request: redirect(reverse("logout"), permanent=True),
    ),
    # Swagger e Redoc
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="redoc-ui"),
    path("api/users/", UserCreateView.as_view(), name="user-create"),
]
