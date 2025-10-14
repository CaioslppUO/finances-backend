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
from .permissions import IsInGroup


# ViewSets
class ExpenseMonthViewSet(viewsets.ModelViewSet):
    queryset = ExpenseMonth.objects.all()
    serializer_class = ExpenseMonthSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["user"]
    permission_classes = [IsAuthenticated, IsInGroup]

    @action(detail=False, url_path="user/(?P<user_id>[^/.]+)")
    def by_user(self, request, user_id=None):
        queryset = self.queryset.filter(fk_user_id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ExpenseTypeViewSet(viewsets.ModelViewSet):
    queryset = ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["user"]
    required_groups = ["user"]
    permission_classes = [IsAuthenticated, IsInGroup]


class ExpenseBudgetViewSet(viewsets.ModelViewSet):
    queryset = ExpenseBudget.objects.all()
    serializer_class = ExpenseBudgetSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["user"]
    permission_classes = [IsAuthenticated, IsInGroup]


class ExpensePaymentViewSet(viewsets.ModelViewSet):
    queryset = ExpensePayment.objects.all()
    serializer_class = ExpensePaymentSerializer
    http_method_names = ["get", "post", "put", "patch"]
    required_groups = ["user"]
    permission_classes = [IsAuthenticated, IsInGroup]
