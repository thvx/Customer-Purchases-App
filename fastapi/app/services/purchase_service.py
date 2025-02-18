from typing import List, Optional
from datetime import date
from statistics import mean
from app.models.purchase import Purchase
from app.repositories.purchase_repo import PurchaseRepository

class PurchaseService:
    def __init__(self, repo: PurchaseRepository):
        self.repo = repo

    def add_purchase(self, purchase: Purchase):
        self.repo.add_purchase(purchase)

    def get_purchases(self, country: Optional[str] = None, start_date: Optional[date] = None, end_date: Optional[date] = None) -> List[Purchase]:
        return self.repo.get_purchases(country, start_date, end_date)

    def compute_kpis(self):
        purchases = self.repo.purchases
        if not purchases:
            return {"mean_per_client": 0, "clients_per_country": {}}
        
        clients = {p.customer_name for p in purchases}
        mean_per_client = sum(p.amount for p in purchases) / len(clients)

        clients_per_country = {}
        for p in purchases:
            clients_per_country.setdefault(p.country, set()).add(p.customer_name)

        return {
            "mean_per_client": mean_per_client,
            "clients_per_country": {k: len(v) for k, v in clients_per_country.items()}
        }
