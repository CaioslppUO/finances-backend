# Django
from rest_framework import viewsets

# Models
from expenses.models import ExpenseMonth

# Serializers
from .serializers import ExpenseMonthSerializer


# Create your views here.
class ExpenseMonthViewSet(viewsets.ModelViewSet):
    queryset = ExpenseMonth.objects.all()
    serializer_class = ExpenseMonthSerializer
