from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models.borrowing import Borrowing
from ..schemas.borrowing_schema import BorrowingSchema
from ..db.database import get_db
from ..utils.response_wrapper import api_response
from models import borrowing

route = APIRouter() 

# CREAT  customer
@route.post("/borrowing/")
def creat_borrowing(borrowing: BorrowingSchema, db: Session = Depends(get_db)):
    if db.query(Borrowing).filter(Borrowing.email == borrowing.email).first():
        raise HTTPException(status_code=400, detail="Email already registerd")
    
    new_customer = Borrowing(**borrowing.dict())
    db.add(get_borrowing)
    db.commit()
    db.refresh(get_borrowing)
    return api_response(
        data=get_borrowing, 
        message="Borrowing already, registered"
        )

# READ single customers
@route.get("/borrowing/{borrowing_id}")
def get_borrowing(borrowing_id: str, db: Session = Depends(get_db)):
    customer =  db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
    return api_response(
        data=borrowing,
        message="Customer retriveed succuessfully"
    )

# UPDATA customer
@route.put("/borrowing/{borrowing_id}")
def updata_borrowing(borrowing_id: str, borrowing_update: BorrowingSchema, db:Session = Depends(get_db)):
    borrowing = db.query(Borrowing).filter(Borrowing.id == borrowing_id).first()
    if borrowing is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    for field, value in borrowing_update.dict(exclude_unset=True).items():
        setattr(borrowing, field, value)

    db.commit()
    db.refresh(borrowing)
    return api_response(
        data=borrowing,
        message="Borrowing updated successfully"
    )

# DELETE customer
@route.delete("/borrowing/{borrowing_id}")
def delete_borrowing(customer_id: str, db: Session = Depends(get_db)):
    customer = db.query(Borrowing).filter(Borrowing.id == borrowing).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(borrowing)
    db.commit()
    return api_response(
        message="Borrowing deleted successfully"
    )