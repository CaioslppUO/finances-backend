# Django
from django.contrib import admin

# Models
from .models import ExpenseMonth


# Registers
@admin.register(ExpenseMonth)
class ExpenseMonthAdmin(admin.ModelAdmin):
    list_display = ("date", "fk_user_id")
    list_filter = ("date", "fk_user_id")
    search_fields = ("date", "fk_user_id")
    ordering = ("date",)
