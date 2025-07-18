from fastapi import APIRouter, HTTPException, Depends, UploadFile
from fastapi.params import File
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user_schema import UserSchema
from ..db.database import get_db
from ..utils.response_wrapper import api_response
from ..utils.cloudinary_uploader import upload_image

route = APIRouter()


# Creat User
@route.post("/user/")
def creat_user(user: UserSchema, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email Already Registerd")
    
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return api_response(
        data=new_user,
        message="User already registerd"
    )

# Read user bay id
@route.get("/user/{user_id}")
def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return api_response(
        data=user,
        message="User retriveed successfully"
    )

# Update user
@route.put("/user/{user_id}")
def updata_user(user_id: str, user_update: UserSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not Found")
    for field, value in user_update.dict(exclude_unset=True).items():
        setattr(user, field, value)
    
    db.commit()
    db.refresh(user)
    return api_response(
        data=user,
        message=" customer updated successfully"
    )

# Delete User
@route.delete("/user/{user_id}")
def delete_user(user_id: str,  db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return api_response(
        message="User deleted successfully"
    )

# upload user profile image
@route.post("/user/{user_id}/profile")
def update_profile_image(
    user_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Upload the image to Cloudinary
    secure_url = upload_image(file, folder="user_profile_images")
    
    # Update the user's profile image URL
    user.profile_image_url = secure_url
    db.commit()
    db.refresh(user)
    
    return api_response(
        data=user,
        message="Profile image updated successfully"
    )