# Django
from rest_framework import serializers

# Models
from .models import ExpenseMonth


# Serializers
class ExpenseMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseMonth
        fields = "__all__"
