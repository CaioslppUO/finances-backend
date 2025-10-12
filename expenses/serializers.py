# Django
from rest_framework import serializers

# Models
from .models import ExpenseMonth, ExpenseType, ExpenseBudget, ExpensePayment


# Serializers
class ExpenseMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseMonth
        fields = "__all__"


class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseType
        fields = "__all__"


class ExpenseBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseBudget
        fields = "__all__"


class ExpensePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensePayment
        fields = "__all__"
