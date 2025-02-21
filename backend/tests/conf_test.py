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
def sample_csv_file():
    # Leer el archivo CSV de prueba desde el sistema de archivos
    with open("sample_purchases.csv", "rb") as file:
        return io.BytesIO(file.read())