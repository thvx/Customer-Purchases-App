from pydantic import BaseModel, ConfigDict
from datetime import date

# Se define el esquema para validar los datos de entrada de la entidad Purchase
class PurchaseSchema(BaseModel):
    customer_name: str
    country: str
    purchase_date: date
    amount: float

    model_config = ConfigDict(orm_mode=True)