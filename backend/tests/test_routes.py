import pytest
from fastapi import status
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    client = TestClient(app)
    # Limpiar la base de datos antes de cada prueba
    client.delete("/purchases/reset/")
    return client

@pytest.fixture
def sample_purchase():
    return {
        "customer_name": "John Doe",
        "country": "USA",
        "purchase_date": "2023-10-01",
        "amount": 100.50
    }

def test_add_purchase(client, sample_purchase):
    # Prueba agregar una compra
    response = client.post("/purchase/", json=sample_purchase)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == sample_purchase

def test_add_bulk_purchases(client, sample_csv):
    # Prueba carga masiva de compras desde un CSV
    files = {"file": ("sample.csv", sample_csv.getvalue(), "text/csv")}
    response = client.post("/purchase/bulk/", files=files)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"added": 2}

def test_get_purchases(client, sample_purchase):
    # Prueba obtener compras filtradas
    client.post("/purchase/", json=sample_purchase)
    response = client.get("/purchases/", params={"country": "USA"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["country"] == "USA"

def test_get_kpis(client, sample_purchase):
    # Prueba obtener KPIs
    client.post("/purchase/", json=sample_purchase)
    response = client.get("/kpis/")
    assert response.status_code == status.HTTP_200_OK
    assert "mean_per_client" in response.json()
    assert "clients_per_country" in response.json()