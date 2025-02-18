from pydantic import BaseModel
from datetime import date

# Se define el esquema para validar los datos de entrada de la entidad Purchase
class PurchaseSchema(BaseModel):
    customer_name: str
    country: str
    purchase_date: date
    amount: float

    class Config:
        orm_mode = True