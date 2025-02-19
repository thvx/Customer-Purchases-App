import io
import csv
from datetime import date
from fastapi import UploadFile, HTTPException
from app.models.purchase import Purchase

class CSVHandler:
    @staticmethod
    async def parse_csv(file: UploadFile):
        if file.content_type not in ["text/csv", "application/vnd.ms-excel"]:
            raise HTTPException(status_code=400, detail="Invalid file format. Only CSV files are allowed")
        
        contents = await file.read()
        decoded = contents.decode("utf-8")
        reader = csv.DictReader(io.StringIO(decoded))

        # Verificar que el archivo tenga las columnas correctas
        required_columns = {"customer_name", "country", "purchase_date", "amount"}
        if not required_columns.issubset(reader.fieldnames):
            raise HTTPException(
                status_code=400,
                detail=f"Invalid CSV format. Required columns: {required_columns}"
            )
        
        purchases = []
        for row in reader:
            try:
                # Validar y convertir los datos
                purchase = Purchase(
                    customer_name=row["customer_name"],
                    country=row["country"],
                    purchase_date=date.fromisoformat(row["purchase_date"]),
                    amount=float(row["amount"])
                )
                purchases.append(purchase)
            except ValueError as e:
                raise HTTPException(
                    status_code=400,
                    detail=f"Error processing row: {row}. Invalid data format: {e}"
                )
        return purchases