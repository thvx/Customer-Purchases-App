from typing import List, Optional
from datetime import date
from app.models.purchase import Purchase

class PurchaseRepository:
    def __init__(self):
        self.purchases = []

    def add_purchase(self, purchase: Purchase):
        self.purchases.append(purchase)

    def get_purchases(self, country: Optional[str] = None, start_date: Optional[date] = None, end_date: Optional[date] = None) -> List[Purchase]:
        filtered = self.purchases
        if country:
            filtered = [p for p in filtered if p.country.lower() == country.lower()]
        if start_date:
            filtered = [p for p in filtered if p.purchase_date >= start_date]
        if end_date:
            filtered = [p for p in filtered if p.purchase_date <= end_date]
        return filtered