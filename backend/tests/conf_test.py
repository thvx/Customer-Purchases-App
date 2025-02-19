import io
import pytest
from fastapi.testclient import TestClient
from main import app
from app.repositories.purchase_repo import PurchaseRepository

@pytest.fixture
def client():
    # Crea un cliente de prueba para FastAPI
    with TestClient(app) as client:
        yield client

@pytest.fixture(autouse=True)
def reset_app_state():
    # Reinicia el estado de la aplicación antes de cada prueba
    PurchaseRepository().purchases.clear()

@pytest.fixture
def sample_purchase():
    # Datos de ejemplo para un registro
    return {
        "customer_name": "John Doe",
        "country": "USA",
        "purchase_date": "2023-10-01",
        "amount": 100.50
    }

@pytest.fixture
def sample_csv():
    # Archivo CSV de ejemplo
    csv_data = """customer_name,country,purchase_date,amount
John Doe,USA,2023-10-01,100.50
Jane Smith,Canada,2023-10-02,200.75"""
    return io.BytesIO(csv_data.encode("utf-8"))