from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Optional
from datetime import date
from app.schemas.purchase_schema import PurchaseSchema
from app.services.purchase_service import PurchaseService
from app.repositories.purchase_repo import PurchaseRepository
from app.utils.csv_handler import CSVHandler

router = APIRouter()
repo = PurchaseRepository()
service = PurchaseService(repo)

@router.post("/purchase/", response_model=PurchaseSchema)
async def add_purchase(purchase: PurchaseSchema):
    service.add_purchase(purchase)
    return purchase

@router.post("/purchase/bulk/")
async def add_bulk_purchases(file: UploadFile = File(...)):
    try:
        purchases = await CSVHandler.parse_csv(file)
        for purchase in purchases:
            service.add_purchase(purchase)
        return JSONResponse(content={"added": len(purchases)})
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

@router.get("/purchases/", response_model=List[PurchaseSchema])
def get_purchases(country: Optional[str] = None, start_date: Optional[date] = None, end_date: Optional[date] = None):
    return service.get_purchases(country, start_date, end_date)

@router.get("/kpis/")
def get_kpis():
    return service.compute_kpis()
