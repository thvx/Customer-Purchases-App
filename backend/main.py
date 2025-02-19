from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Customer Purchases API")

app.include_router(router)