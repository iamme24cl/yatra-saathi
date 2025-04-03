import datetime
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate

def create_company(company_data: CompanyCreate, db: Session) -> Company:
    company = Company(**company_data.model_dump())
    db.add(company)
    db.commit()
    db.refresh(company)
    return company

def get_company_by_id(company_id: UUID, db: Session) -> Company | None:
    return db.query(Company).filter(Company.id == company_id).first()

def update_company(company: Company, updates: CompanyUpdate, db: Session) -> Company:
    for field, value in updates.model_dump(exculde_unset=True).item():
        setattr(company, field, value)
    
    db.commit()
    db.refresh(company)
    return company 

def delete_company(company: Company, db: Session):
    company.deleted_at = datetime.datetime.now(datetime.timezone.utc)
    db.commit()
    db.refresh(company)