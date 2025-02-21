import requests
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()
API_BASE_URL = os.getenv('API_URL')

def add_purchase(purchase_data):
    response = requests.post(f"{API_BASE_URL}/purchase/", json=purchase_data)
    return response.status_code == 200

def bulk_upload_purchases(file):
    files = {"file": (file.name, file.getvalue(), "text/csv")}
    response = requests.post(f"{API_BASE_URL}/purchase/bulk/", files=files)
    return response.status_code == 200

def get_filtered_purchases(country=None, start_date=None, end_date=None):
    params = {}
    if country:
        params["country"] = country
    if start_date:
        params["start_date"] = start_date.isoformat() if isinstance(start_date, date) else start_date
    if end_date:
        params["end_date"] = end_date.isoformat() if isinstance(end_date, date) else end_date
    response = requests.get(f"{API_BASE_URL}/purchases/", params=params)
    return response.json()

def get_kpis():
    response = requests.get(f"{API_BASE_URL}/kpis/")
    return response.json()

def get_forecast(periods: int = 12):
    response = requests.get(f"{API_BASE_URL}/forecast/", params={"periods": periods})
    return response.json()