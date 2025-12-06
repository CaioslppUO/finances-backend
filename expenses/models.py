# Django
from django.db import models
from django.contrib.auth.models import User

class ExpenseType(models.Model):
    """
    Personal expense types.
    """

    expense_type_id = models.AutoField(primary_key=True)
    fk_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="expense_types"
    )
    type = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["fk_user_id", "type"], name="unique_user_expense_type"
            )
        ]

    def __str__(self):
        return f"{self.type} - Ativo: {self.is_active}"


class ExpenseBudget(models.Model):
    """
    Personal expense budgets.
    """

    expense_budget_id = models.AutoField(primary_key=True)
    fk_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="expense_budgets"
    )
    budget = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["fk_user_id", "budget"], name="unique_user_expense_budget"
            )
        ]

    def __str__(self):
        return f"{self.budget} - Ativo: {self.is_active}"


class ExpensePayment(models.Model):
    """
    Personal expense payments methods.
    """

    expense_payment_id = models.AutoField(primary_key=True)
    fk_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="expense_payments"
    )
    payment = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["fk_user_id", "payment"], name="unique_user_expense_payment"
            )
        ]

    def __str__(self):
        return f"{self.payment} - Ativo: {self.is_active}"


class Expense(models.Model):
    """
    A user personal expense.
    """

    expense_id = models.AutoField(primary_key=True)
    fk_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="expenses"
    )
    date = models.DateField()
    description = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    fk_type_id = models.ForeignKey(
        ExpenseType,
        on_delete=models.SET_NULL,
        related_name="expenses",
        null=True,
        blank=True,
    )
    fk_budget_id = models.ForeignKey(
        ExpenseBudget,
        on_delete=models.SET_NULL,
        related_name="expenses",
        null=True,
        blank=True,
    )
    fk_payment_id = models.ForeignKey(
        ExpensePayment,
        on_delete=models.SET_NULL,
        related_name="expenses",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.date} - {self.fk_user_id.username} - {self.description} - {self.value}"
