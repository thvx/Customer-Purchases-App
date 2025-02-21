import pytest
from datetime import date
from app.services.purchase_service import PurchaseService
from app.repositories.purchase_repo import PurchaseRepository
from app.models.purchase import Purchase

@pytest.fixture
def repo():
    return PurchaseRepository()

@pytest.fixture
def service(repo):
    return PurchaseService(repo)

def test_add_purchase_service(service):
    purchase = Purchase("John Doe", "USA", date(2023, 10, 1), 100.50)
    service.add_purchase(purchase)
    assert len(service.repo.purchases) == 1

def test_get_purchases_service(service):
    purchase1 = Purchase("John Doe", "USA", date(2023, 10, 1), 100.50)
    purchase2 = Purchase("Jane Smith", "Canada", date(2023, 10, 2), 200.75)
    service.add_purchase(purchase1)
    service.add_purchase(purchase2)
    purchases = service.get_purchases(country="USA")
    assert len(purchases) == 1
    assert purchases[0].country == "USA"

def test_compute_kpis(service):
    purchase1 = Purchase("John Doe", "USA", date(2023, 10, 1), 100.50)
    purchase2 = Purchase("Jane Smith", "Canada", date(2023, 10, 2), 200.75)
    service.add_purchase(purchase1)
    service.add_purchase(purchase2)
    kpis = service.compute_kpis()
    assert kpis["mean_per_client"] == 150.625
    assert kpis["clients_per_country"] == {"USA": 1, "Canada": 1}