import requests

API_BASE_URL = "http://127.0.0.1:8000"  # URL de la API de FastAPI

def add_purchase(purchase_data):
    response = requests.post(f"{API_BASE_URL}/purchase/", json=purchase_data)
    return response.status_code == 200

def bulk_upload_purchases(file):
    files = {"file": (file.name, file.getvalue(), "text/csv")}
    response = requests.post(f"{API_BASE_URL}/purchase/bulk/", files=files)
    return response.status_code == 200

def get_filtered_purchases(date=None, country=None):
    params = {}
    if date:
        params["date"] = date
    if country:
        params["country"] = country
    response = requests.get(f"{API_BASE_URL}/purchase/", params=params)
    return response.json()

def get_kpis():
    response = requests.get(f"{API_BASE_URL}/kpis/")
    return response.json()