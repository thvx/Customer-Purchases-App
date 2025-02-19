from dataclasses import dataclass
from datetime import date

@dataclass
class Purchase:
    customer_name: str
    country: str
    purchase_date: date
    amount: float

@dataclass
class KPIs:
    mean_purchases_per_client: float
    clients_per_country: dict
    forecast_sales: float