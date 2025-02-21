import pytest
from fastapi import status
from fastapi.testclient import TestClient
from main import app
from .conf_test import sample_purchase, sample_csv_file

@pytest.fixture
def client():
    client = TestClient(app)
    return client

def test_add_bulk_purchases(client, sample_csv_file):
    # Prueba carga masiva de compras desde el archivo sample_purchases.csv
    files = {"file": ("sample_purchases.csv", sample_csv_file, "text/csv")}
    response = client.post("/purchase/bulk/", files=files)
    assert response.status_code == status.HTTP_200_OK
    # Verificar que se cargaron los datos correctamente
    purchases = client.get("/purchases/").json()
    assert len(purchases) > 0

def test_get_purchases(client, sample_purchase):
    # Prueba obtener compras filtradas
    client.post("/purchase/", json=sample_purchase)
    response = client.get("/purchases/", params={"country": "USA"})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1
    assert response.json()[0]["country"] == "USA"

def test_add_purchase(client, sample_purchase):
    # Prueba agregar una compra
    response = client.post("/purchase/", json=sample_purchase)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == sample_purchase

def test_get_kpis(client, sample_purchase):
    # Prueba obtener KPIs
    client.post("/purchase/", json=sample_purchase)
    response = client.get("/kpis/")
    assert response.status_code == status.HTTP_200_OK
    assert "mean_per_client" in response.json()
    assert "clients_per_country" in response.json()