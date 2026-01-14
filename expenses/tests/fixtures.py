# Django
from django.contrib.auth.models import User

# Pytest
import pytest

# Models
from expenses.models import ExpenseType, ExpenseBudget, ExpensePayment, Expense

@pytest.fixture
def expense_type_fixture(user: User):
    return [
        ExpenseType.objects.create(fk_user_id=user, type="Expense Type 1"),
        ExpenseType.objects.create(fk_user_id=user, type="Expense Type 2"),
        ExpenseType.objects.create(fk_user_id=user, type="Expense Type 3"),
    ]
    

@pytest.fixture
def expense_budget_fixture(user: User):
    return [
        ExpenseBudget.objects.create(fk_user_id=user, budget="Expense Budget 1"),
        ExpenseBudget.objects.create(fk_user_id=user, budget="Expense Budget 2"),
        ExpenseBudget.objects.create(fk_user_id=user, budget="Expense Budget 3"),
    ]

@pytest.fixture
def expense_payment_fixture(user: User):
    return [
        ExpensePayment.objects.create(fk_user_id=user, payment="Expense Payment 1"),
        ExpensePayment.objects.create(fk_user_id=user, payment="Expense Payment 2"),
        ExpensePayment.objects.create(fk_user_id=user, payment="Expense Payment 3"),
    ]

@pytest.fixture
def expense_fixture(user: User, expense_type_fixture, expense_budget_fixture, expense_payment_fixture):
    return [
        Expense.objects.create(fk_user_id=user,
            description="Expense 1",
            value=100.52,
            date="2026-01-01",
            fk_type_id=expense_type_fixture[0],
            fk_budget_id=expense_budget_fixture[0],
            fk_payment_id=expense_payment_fixture[0],
        ),
        Expense.objects.create(fk_user_id=user,
            description="Expense 2",
            value=39.12,
            date="2026-01-15",
            fk_type_id=expense_type_fixture[1],
            fk_budget_id=expense_budget_fixture[1],
            fk_payment_id=expense_payment_fixture[1],
        ),
        Expense.objects.create(fk_user_id=user,
            description="Expense 3",
            value=20,
            date="2026-01-09",
            fk_type_id=expense_type_fixture[2],
            fk_budget_id=expense_budget_fixture[2],
            fk_payment_id=expense_payment_fixture[2],
        ),
    ]
    