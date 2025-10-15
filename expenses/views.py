# Django
from rest_framework import viewsets

# Django Rest
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

# Models
from expenses.models import ExpenseMonth, ExpenseType, ExpenseBudget, ExpensePayment

# Serializers
from .serializers import (
    ExpenseMonthSerializer,
    ExpenseTypeSerializer,
    ExpenseBudgetSerializer,
    ExpensePaymentSerializer,
)

# Permissions
from .permissions import IsInGroup, user_group_actions


# ViewSets
class ExpenseMonthViewSet(viewsets.ModelViewSet):
    queryset = ExpenseMonth.objects.all()
    serializer_class = ExpenseMonthSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["admin"]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        user_groups = [group.name for group in user.groups.all()]

        if user.is_superuser:
            response = super().list(request, *args, **kwargs)
        elif "user" in user_groups:
            queryset = self.queryset.filter(fk_user_id=user.id)
            serializer = self.get_serializer(queryset, many=True)
            response = Response(serializer.data)

        return response

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class ExpenseTypeViewSet(viewsets.ModelViewSet):
    queryset = ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["admin"]
    permission_classes = [IsAuthenticated, IsInGroup]

    def get_permissions(self):
        if self.action in user_group_actions:
            return [IsAuthenticated()]  # User permissions

        # Default controller
        return super().get_permissions()

    @action(detail=False, url_path="user", methods=["get"])
    def by_user(self, request):
        queryset = self.queryset.filter(fk_user_id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ExpenseBudgetViewSet(viewsets.ModelViewSet):
    queryset = ExpenseBudget.objects.all()
    serializer_class = ExpenseBudgetSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["admin"]
    permission_classes = [IsAuthenticated, IsInGroup]

    def get_permissions(self):
        if self.action in user_group_actions:
            return [IsAuthenticated()]  # User permissions

        # Default controller
        return super().get_permissions()

    @action(detail=False, url_path="user", methods=["get"])
    def by_user(self, request):
        queryset = self.queryset.filter(fk_user_id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ExpensePaymentViewSet(viewsets.ModelViewSet):
    queryset = ExpensePayment.objects.all()
    serializer_class = ExpensePaymentSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["admin"]
    permission_classes = [IsAuthenticated, IsInGroup]

    def get_permissions(self):
        if self.action in user_group_actions:
            return [IsAuthenticated()]  # User permissions

        # Default controller
        return super().get_permissions()

    @action(detail=False, url_path="user", methods=["get"])
    def by_user(self, request):
        queryset = self.queryset.filter(fk_user_id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
