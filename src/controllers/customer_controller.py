from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models.customer import Customer
from ..schemas.customer_schema import CustomerSchema
from ..db.database import get_db
from ..utils.response_wrapper import api_response

route = APIRouter()

# CREAT  customer
@route.post("/customer/")
def creat_customer(customer: CustomerSchema, db: Session = Depends(get_db)):
    if db.query(Customer).filter(Customer.email == customer.email).first():
        raise HTTPException(status_code=400, detail="Email already registerd")
    
    new_customer = Customer(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return api_response(
        data=new_customer, 
        message="Customer already, registered"
        )

# READ single customers
@route.get("/customer/{customer_id}")
def get_customer(customer_id: str, db: Session = Depends(get_db)):
    customer =  db.query(Customer).filter(Customer.id == customer_id).first()
    return api_response(
        data=customer,
        message="Customer retriveed succuessfully"
    )

# UPDATA customer
@route.put("/customer/{customer_id}")
def updata_customer(customer_id: str, customer_update: CustomerSchema, db:Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    for field, value in customer_update.dict(exclude_unset=True).items():
        setattr(customer, field, value)

    db.commit()
    db.refresh(customer)
    return api_response(
        data=customer,
        message="Customer updated successfully"
    )

# DELETE customer
@route.delete("/customer/{customer_id}")
def delete_customer(customer_id: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(customer)
    db.commit()
    return api_response(
        message="Customer deleted successfully"
    )