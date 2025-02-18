from datetime import date

# Se define la entidad Purchase en el sistema
class Purchase:
    def __init__(self, customer_name: str, country: str, purchase_date: date, amount: float):
        self.customer_name = customer_name
        self.country = country
        self.purchase_date = purchase_date
        self.amount = amount