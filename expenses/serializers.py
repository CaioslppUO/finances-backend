# Django
from rest_framework import serializers

# Models
from .models import ExpenseMonth, ExpenseType, ExpenseBudget, ExpensePayment


# Serializers
class ExpenseMonthSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return {"username": obj.fk_user_id.username, "user_id": obj.fk_user_id.id}

    class Meta:
        model = ExpenseMonth
        fields = (
            "expense_month_id",
            "date",
            "user",
        )


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
