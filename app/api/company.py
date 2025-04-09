from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID

from app.database import get_db
from app.schemas.company import CompanyCreate, CompanyUpdate
from app.schemas.company import CompanyResponse
from app.services import company_service
from app.dependencies import get_current_admin
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=CompanyResponse)
def create_company(company: CompanyCreate, db: Session = Depends(get_db), user: User = Depends(get_current_admin)):
    return company_service.create_company(company, db)

@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(company_id: UUID, db: Session = Depends(get_db)):
    company = company_service.get_company_by_id(company_id, db)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.put("/{company_id}", response_model=CompanyResponse)
def update_company(company_id: UUID, updates: CompanyUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_admin)):
    company = company_service.get_company_by_id(company_id, db)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company_service.update_company(company, updates, db)

@router.delete("/{company_id}")
def delete_company(company_id: UUID, db: Session = Depends(get_db), user: User = Depends(get_current_admin)):
    company = company_service.get_company_by_id(company_id, db)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    company_service.delete_company(company, db)
    return {"message": "Company deleted successfully"}
