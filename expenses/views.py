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
    permission_classes = [IsAuthenticated, IsInGroup]

    @action(detail=False, url_path="user")
    def by_user(self, request):
        print(request.user.id)
        queryset = self.queryset.filter(fk_user_id=request.user.id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_permissions(self):
        if self.action in user_group_actions:
            return [IsAuthenticated()]  # User permissions

        # Default controller
        return super().get_permissions()


class ExpenseTypeViewSet(viewsets.ModelViewSet):
    queryset = ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer
    http_method_names = ["get", "post", "put", "patch"]
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
    required_groups = ["admin"]
    permission_classes = [IsAuthenticated, IsInGroup]
