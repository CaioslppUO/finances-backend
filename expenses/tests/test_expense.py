# Django
from django.urls import reverse
from rest_framework.test import APIClient

# Pytest
import pytest

@pytest.mark.django_db
def test_create_expense(auth_client: APIClient, expense_payment_fixture, expense_budget_fixture, expense_type_fixture):
    # Rota
    url = reverse("expenses-list")

    # Cria uma despesa para testar depois
    payload = {
        "description": "New Expense Description",
        "value": "125.56",
        "date": "2026-01-01",
        "fk_type_id": 1,
        "fk_budget_id": 1,
        "fk_payment_id": 1
    }
    response = auth_client.post(url, payload, format="json")

    # Testes
    assert response.status_code == 201
    assert response.data["expense_id"] == 1
    assert response.data["description"] == "New Expense Description"
    assert response.data["value"] == "125.56"
    assert response.data["date"] == "2026-01-01"
    assert response.data["fk_type_id"] == 1
    assert response.data["fk_budget_id"] == 1
    assert response.data["fk_payment_id"] == 1

@pytest.mark.django_db
def test_get_expense(auth_client: APIClient, expense_fixture) -> None:
    # Rota
    url = reverse("expenses-list")
    response = auth_client.get(url)

    # Testes
    assert response.status_code == 200
    assert len(response.data) == 3

    # Verifica os dados preenchidos pelas fixtures
    assert response.data[0]["description"] == "Expense 1"
    assert response.data[0]["value"] == "100.52"
    assert response.data[0]["date"] == "2026-01-01"
    assert response.data[0]["fk_type_id"] == 1
    assert response.data[0]["fk_budget_id"] == 1
    assert response.data[0]["fk_payment_id"] == 1

    assert response.data[1]["description"] == "Expense 2"
    assert response.data[1]["value"] == "39.12"
    assert response.data[1]["date"] == "2026-01-15"
    assert response.data[1]["fk_type_id"] == 2
    assert response.data[1]["fk_budget_id"] == 2
    assert response.data[1]["fk_payment_id"] == 2

    assert response.data[2]["description"] == "Expense 3"
    assert response.data[2]["value"] == "20.00"
    assert response.data[2]["date"] == "2026-01-09"
    assert response.data[2]["fk_type_id"] == 3
    assert response.data[2]["fk_budget_id"] == 3
    assert response.data[2]["fk_payment_id"] == 3

@pytest.mark.django_db
def test_update_expense(auth_client: APIClient, expense_fixture) -> None:
    # Rota
    url = reverse("expenses-list")

    # Antes de Editar
    before_edit = auth_client.get(url)
    assert before_edit.data[0]["description"] == "Expense 1"

    # Edição
    payload = {
        "description": "Expense Description 1 Updated"
    }
    response_edit = auth_client.patch(url + str(before_edit.data[0]["expense_id"])  + "/", payload, format="json")
    assert response_edit.status_code == 200
    assert response_edit.data["description"] == "Expense Description 1 Updated"
    
    # Depois de editar
    after_edit = auth_client.get(url)
    assert after_edit.data[0]["description"] == "Expense Description 1 Updated"
    assert after_edit.data[1]["description"] == "Expense 2"
    assert after_edit.data[2]["description"] == "Expense 3"

@pytest.mark.django_db
def test_delete_expense(auth_client: APIClient, expense_fixture) -> None:
    # Rota
    url = reverse("expenses-list")

    # Antes de Editar
    before_edit = auth_client.get(url)
    assert before_edit.data[0]["description"] == "Expense 1"

    # Deleção
    response_edit = auth_client.delete(url + str(before_edit.data[0]["expense_id"])  + "/")
    assert response_edit.status_code == 204
    
    # Depois de deletar
    after_delete = auth_client.get(url)
    assert after_delete.data[0]["description"] == "Expense 2"
    assert after_delete.data[1]["description"] == "Expense 3"
    assert len(after_delete.data) == 2