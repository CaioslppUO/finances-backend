# Django
from django.contrib.auth.models import User

# Pytest
import pytest

# Models
from expenses.models import ExpenseType

@pytest.fixture
def expense_type_fixture(user: User):
    return ExpenseType.objects.bulk_create(
        [
            ExpenseType(fk_user_id=user, type="Expense Type 1"),
            ExpenseType(fk_user_id=user, type="Expense Type 2"),
            ExpenseType(fk_user_id=user, type="Expense Type 3"),
        ]
    )