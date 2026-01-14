# Django
from django.contrib.auth.models import User

# Pytest
import pytest

# Models
from expenses.models import ExpenseType, ExpenseBudget, ExpensePayment

@pytest.fixture
def expense_type_fixture(user: User):
    return ExpenseType.objects.bulk_create(
        [
            ExpenseType(fk_user_id=user, type="Expense Type 1"),
            ExpenseType(fk_user_id=user, type="Expense Type 2"),
            ExpenseType(fk_user_id=user, type="Expense Type 3"),
        ]
    )

@pytest.fixture
def expense_budget_fixture(user: User):
    return ExpenseBudget.objects.bulk_create(
        [
            ExpenseBudget(fk_user_id=user, budget="Expense Budget 1"),
            ExpenseBudget(fk_user_id=user, budget="Expense Budget 2"),
            ExpenseBudget(fk_user_id=user, budget="Expense Budget 3"),
        ]
    )

@pytest.fixture
def expense_payment_fixture(user: User):
    return ExpensePayment.objects.bulk_create(
        [
            ExpensePayment(fk_user_id=user, payment="Expense Payment 1"),
            ExpensePayment(fk_user_id=user, payment="Expense Payment 2"),
            ExpensePayment(fk_user_id=user, payment="Expense Payment 3"),
        ]
    )