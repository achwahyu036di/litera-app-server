from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user_schema import UserSchema
from ..db.database import get_db
from ..utils.response_wrapper import api_response
import bcrypt

route = APIRouter()

# auth signup
@route.post("/signup/") 
def signup(user: UserSchema, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email Already Registered")
    
    password_hash = bcrypt.hashpw(user.password, bcrypt.gensalt())
    user.password = password_hash
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return api_response(
        data=new_user,
        message="User successfully registered"
    )

# auth login
@route.post("/login/")
def login(user: UserSchema, db: Session = Depends(get_db)): 
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not db_user.verify_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid email")
    
    # decode the password
    if not bcrypt.checkpw(user.password.encode, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")
    
    return api_response(
        data=db_user,
        message="Login successful"
    )