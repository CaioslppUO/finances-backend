# Django
from django.urls import reverse
from rest_framework.test import APIClient

# Pytest
import pytest

@pytest.mark.django_db
def test_create_expense(auth_client: APIClient):
    # Rota
    url = reverse("expenses_types-list")

    # Cria um tipo para testar depois
    payload = {
        "type": "New Expense Type"
    }
    response = auth_client.post(url, payload, format="json")

    # Testes
    assert response.status_code == 201
    assert response.data["fk_user_id"] == 1
    assert response.data["type"] == "New Expense Type"
    assert response.data["is_active"] == True

@pytest.mark.django_db
def test_get_expense(auth_client: APIClient, expense_type_fixture):
    # Rota
    url = reverse("expenses_types-list")
    response = auth_client.get(url)

    # Testes
    assert response.status_code == 200
    assert len(response.data) == 3

    # Verifica os dados preenchidos pelas fixtures
    assert response.data[0]["type"] == "Expense Type 1"
    assert response.data[1]["type"] == "Expense Type 2"
    assert response.data[2]["type"] == "Expense Type 3"

@pytest.mark.django_db
def test_update_expense(auth_client: APIClient, expense_type_fixture):
    # Rota
    url = reverse("expenses_types-list")

    # Antes de Editar
    before_edit = auth_client.get(url)
    assert before_edit.data[0]["type"] == "Expense Type 1"

    # Edição
    payload = {
        "type": "Expense Type 1 Updated"
    }
    response_edit = auth_client.patch(url + str(before_edit.data[0]["expense_type_id"])  + "/", payload, format="json")
    assert response_edit.status_code == 200
    assert response_edit.data["type"] == "Expense Type 1 Updated"
    
    # Depois de editar
    after_edit = auth_client.get(url)
    assert after_edit.data[0]["type"] == "Expense Type 1 Updated"
    assert after_edit.data[1]["type"] == "Expense Type 2"
    assert after_edit.data[2]["type"] == "Expense Type 3"

@pytest.mark.django_db
def test_delete_expense(auth_client: APIClient, expense_type_fixture):
    # Rota
    url = reverse("expenses_types-list")

    # Antes de Editar
    before_edit = auth_client.get(url)
    assert before_edit.data[0]["type"] == "Expense Type 1"

    # Deleção
    response_edit = auth_client.delete(url + str(before_edit.data[0]["expense_type_id"])  + "/")
    assert response_edit.status_code == 204
    
    # Depois de deletar
    after_delete = auth_client.get(url)
    assert after_delete.data[0]["type"] == "Expense Type 2"
    assert after_delete.data[1]["type"] == "Expense Type 5"
    assert len(after_delete.data) == 2