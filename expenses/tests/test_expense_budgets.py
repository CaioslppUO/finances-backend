# Django
from django.urls import reverse
from django.db import IntegrityError
from rest_framework.test import APIClient

# Pytest
import pytest

# Models
from expenses.models import ExpenseBudget


@pytest.mark.django_db
def test_create_expense_budget(auth_client: APIClient):
    # Rota
    url = reverse("expenses_budgets-list")

    # Cria um tipo para testar depois
    payload = {
        "budget": "New Expense Budget"
    }
    response = auth_client.post(url, payload, format="json")

    # Testes
    assert response.status_code == 201
    assert response.data["fk_user_id"] == 1
    assert response.data["budget"] == "New Expense Budget"
    assert response.data["is_active"] == True

@pytest.mark.django_db
def test_get_expense_budget(auth_client: APIClient, expense_budget_fixture) -> None:
    # Rota
    url = reverse("expenses_budgets-list")
    response = auth_client.get(url)

    # Testes
    assert response.status_code == 200
    assert len(response.data) == 3

    # Verifica os dados preenchidos pelas fixtures
    assert response.data[0]["budget"] == "Expense Budget 1"
    assert response.data[1]["budget"] == "Expense Budget 2"
    assert response.data[2]["budget"] == "Expense Budget 3"

@pytest.mark.django_db
def test_update_expense_budget(auth_client: APIClient, expense_budget_fixture) -> None:
    # Rota
    url = reverse("expenses_budgets-list")

    # Antes de Editar
    before_edit = auth_client.get(url)
    assert before_edit.data[0]["budget"] == "Expense Budget 1"

    # Edição
    payload = {
        "budget": "Expense Budget 1 Updated"
    }
    response_edit = auth_client.patch(url + str(before_edit.data[0]["expense_budget_id"])  + "/", payload, format="json")
    assert response_edit.status_code == 200
    assert response_edit.data["budget"] == "Expense Budget 1 Updated"
    
    # Depois de editar
    after_edit = auth_client.get(url)
    assert after_edit.data[0]["budget"] == "Expense Budget 1 Updated"
    assert after_edit.data[1]["budget"] == "Expense Budget 2"
    assert after_edit.data[2]["budget"] == "Expense Budget 3"

@pytest.mark.django_db
def test_delete_expense_type(auth_client: APIClient, expense_budget_fixture) -> None:
    # Rota
    url = reverse("expenses_budgets-list")

    # Antes de Editar
    before_edit = auth_client.get(url)
    assert before_edit.data[0]["budget"] == "Expense Budget 1"

    # Deleção
    response_edit = auth_client.delete(url + str(before_edit.data[0]["expense_budget_id"])  + "/")
    assert response_edit.status_code == 204
    
    # Depois de deletar
    after_delete = auth_client.get(url)
    assert after_delete.data[0]["budget"] == "Expense Budget 2"
    assert after_delete.data[1]["budget"] == "Expense Budget 3"
    assert len(after_delete.data) == 2

@pytest.mark.django_db(transaction=True)
def test_block_duplicated_budget_creation(auth_client: APIClient) -> None:
    # Rota
    url = reverse("expenses_budgets-list")

    # Cria um orçamento para testar depois
    payload = {
        "budget": "Repeated Expense Budget"
    }
    response = auth_client.post(url, payload, format="json")

    assert response.status_code == 201
    assert response.data["budget"] == "Repeated Expense Budget"
    assert response.data["is_active"] == True

    payload = {
        "budget": "Repeated Expense Budget"
    }

    with pytest.raises(IntegrityError):
        response2 = auth_client.post(url, payload, format="json")
    
    # Teste
    assert ExpenseBudget.objects.count() == 1