import pytest
from datetime import date
from app.repositories.purchase_repo import PurchaseRepository
from app.models.purchase import Purchase

@pytest.fixture
def repo():
    return PurchaseRepository()

def test_add_purchase(repo):
    # Prueba agregar una compra al repositorio
    purchase = Purchase(
        customer_name="John Doe",
        country="USA",
        purchase_date=date(2023, 10, 1),
        amount=100.50
    )
    repo.add_purchase(purchase)
    assert len(repo.purchases) == 1

def test_get_purchases(repo):
    # Prueba obtener compras filtradas
    purchase1 = Purchase(
        customer_name="John Doe",
        country="USA",
        purchase_date=date(2023, 10, 1),
        amount=100.50
    )
    purchase2 = Purchase(
        customer_name="Jane Smith",
        country="Canada",
        purchase_date=date(2023, 10, 2),
        amount=200.75
    )
    repo.add_purchase(purchase1)
    repo.add_purchase(purchase2)
    purchases = repo.get_purchases(country="USA")
    assert len(purchases) == 1
    assert purchases[0].country == "USA"