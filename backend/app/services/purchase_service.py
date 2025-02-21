from http.client import HTTPException
from typing import List, Optional, Dict
from datetime import date, timedelta
from statistics import mean
from app.models.purchase import Purchase
from app.repositories.purchase_repo import PurchaseRepository
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import warnings

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
    
    def forecast_sales(self, periods: int = 12) -> Dict[date, float]:
        # Predicción de ventas usando el modelo ARIMA
        purchases = self.repo.purchases
        if not purchases:
            return {}
        
        # Agrupar las compras por fecha y sumar los montos
        sales_by_date = {}
        for purchase in purchases:
            sales_by_date[purchase.purchase_date] = sales_by_date.get(purchase.purchase_date, 0) + purchase.amount

        # Convertir a un DataFrame de pandas para manipular los datos 
        df = pd.DataFrame(list(sales_by_date.items()), columns=["date", "amount"])
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index("date")
        df = df.sort_index()

        # Ajustar modelo ARIMA
        warnings.filterwarnings("ignore")
        try:
            model = ARIMA(df["amount"], order=(5, 1, 0))  # parametros (p, d, q)
            model_fit = model.fit()
            forecast = model_fit.forecast(steps=periods)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fitting ARIMA model: {e}")

        # Generar fechas para los periodos de pronóstico
        last_date = df.index[-1]
        forecast_dates = [last_date + timedelta(days=i) for i in range(1, periods + 1)]

        # Combinar las fechas y valores predecidos
        forecast_dict = {date.strftime("%Y-%m-%d"): value for date, value in zip(forecast_dates, forecast)}

        return forecast_dict