from fastapi import FastAPI
from app.controllers.customer_controller import route as customer_router
from app.controllers.user_controller import route as user_router
from app.db.database import create_tabels

app = FastAPI()

app.include_router(customer_router, prefix="/api", tags=["Customers"])
app.include_router(user_router, prefix="/api", tags=["Users"])

create_tabels()

@app.get("/")
def root():
    return {"message": "Welcome to the FasyAPI CRUD API"}