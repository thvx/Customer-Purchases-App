import io
import csv
from datetime import date
from fastapi import UploadFile, HTTPException
from app.models.purchase import Purchase

class CSVHandler:
    @staticmethod
    async def parse_csv(file: UploadFile):
        if file.content_type not in ["text/csv"]:
            raise HTTPException(status_code=400, detail="Invalid file format")
        
        contents = await file.read()
        decoded = contents.decode("utf-8")
        reader = csv.DictReader(io.StringIO(decoded))
        
        purchases = []
        for row in reader:
            try:
                purchase = Purchase(
                    customer_name=row["customer_name"],
                    country=row["country"],
                    purchase_date=date.fromisoformat(row["purchase_date"]),
                    amount=float(row["amount"])
                )
                purchases.append(purchase)
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Error processing row: {row} - {e}")
        
        return purchases