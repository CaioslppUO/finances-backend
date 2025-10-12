# Django
from rest_framework import viewsets

# Django Rest
from rest_framework.response import Response

# Models
from expenses.models import ExpenseMonth, ExpenseType, ExpenseBudget, ExpensePayment

# Serializers
from .serializers import (
    ExpenseMonthSerializer,
    ExpenseTypeSerializer,
    ExpenseBudgetSerializer,
    ExpensePaymentSerializer,
)


# ViewSets
class ExpenseMonthViewSet(viewsets.ModelViewSet):
    queryset = ExpenseMonth.objects.all()
    serializer_class = ExpenseMonthSerializer


class ExpenseTypeViewSet(viewsets.ModelViewSet):
    queryset = ExpenseType.objects.all()
    serializer_class = ExpenseTypeSerializer
    http_method_names = ["get", "post", "put", "patch"]


class ExpenseBudgetViewSet(viewsets.ModelViewSet):
    queryset = ExpenseBudget.objects.all()
    serializer_class = ExpenseBudgetSerializer
    http_method_names = ["get", "post", "put", "patch"]


class ExpensePaymentViewSet(viewsets.ModelViewSet):
    queryset = ExpensePayment.objects.all()
    serializer_class = ExpensePaymentSerializer
    http_method_names = ["get", "post", "put", "patch"]
