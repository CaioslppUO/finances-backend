# Django
from django.contrib import admin

# Models
from .models import ExpenseType, ExpenseBudget, ExpensePayment, Expense


# Registers
@admin.register(ExpenseType)
class ExpenseTypeAdmin(admin.ModelAdmin):
    list_display = ("expense_type_id", "type", "fk_user_id", "is_active")
    list_filter = ("expense_type_id", "type", "fk_user_id", "is_active")
    search_fields = ("expense_type_id", "type", "fk_user_id", "is_active")
    ordering = ("expense_type_id", "type", "is_active")


@admin.register(ExpenseBudget)
class ExpenseBudgetAdmin(admin.ModelAdmin):
    list_display = ("expense_budget_id", "budget", "fk_user_id", "is_active")
    list_filter = ("expense_budget_id", "budget", "fk_user_id", "is_active")
    search_fields = ("expense_budget_id", "budget", "fk_user_id", "is_active")
    ordering = ("expense_budget_id", "budget", "is_active")


@admin.register(ExpensePayment)
class ExpensePaymentAdmin(admin.ModelAdmin):
    list_display = ("expense_payment_id", "payment", "fk_user_id", "is_active")
    list_filter = ("expense_payment_id", "payment", "fk_user_id", "is_active")
    search_fields = ("expense_payment_id", "payment", "fk_user_id", "is_active")
    ordering = ("expense_payment_id", "payment", "is_active")


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "expense_id",
        "fk_user_id",
        "date",
        "description",
        "value",
    )
    list_filter = (
        "expense_id",
        "fk_user_id",
        "date",
    )
    search_fields = (
        "expense_id",
        "fk_user_id",
        "date",
    )
    ordering = ("expense_id", "fk_user_id", "date")
