# Django
from rest_framework import serializers

# Models
from .models import ExpenseType, ExpenseBudget, ExpensePayment, Expense

class ExpenseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseType
        fields = "__all__"
        extra_kwargs = {
            'fk_user_id': {'read_only': True}
        }


class ExpenseBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseBudget
        fields = "__all__"
        extra_kwargs = {
            'fk_user_id': {'read_only': True}
        }


class ExpensePaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensePayment
        fields = "__all__"
        extra_kwargs = {
            'fk_user_id': {'read_only': True}
        }

class ExpenseSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='fk_type_id.type', read_only=True)
    budget_name = serializers.CharField(source='fk_budget_id.budget', read_only=True)
    payment_method = serializers.CharField(source='fk_payment_id.payment', read_only=True)

    class Meta:
        model = Expense
        fields = (
            "expense_id",
            "description",
            "value",
            "date", 
            "type_name",
            "budget_name",
            "payment_method",
            "fk_type_id",
            "fk_budget_id",
            "fk_payment_id",
        )
        extra_kwargs = {
            'fk_user_id': {'read_only': True}
        }