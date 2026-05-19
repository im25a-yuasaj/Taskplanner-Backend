'''
route for user
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.user import User
from schemas.user import UserSchema, CreateUserSchema
from typing import List

router = APIRouter(prefix="/user", tags=["user"])

@router.get('/', response_model=List[UserSchema])
def get_all_users(db: Session = Depends(get_db)):
    db_users = db.query(User).all()
    return db_users

@router.get('/{user_id}', response_model=UserSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.BenutzerID == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post('/create-user', response_model=UserSchema)
def create_user(user: CreateUserSchema, db: Session = Depends(get_db)):
    db_user = User(
        BenutzerName=user.BenutzerName,
        BenutzerPWD=user.BenutzerPWD,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post('/update-username/{user_id}/{new_name}', response_model=UserSchema)
def update_username(user_id: int, new_name: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.BenutzerID == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.BenutzerName = new_name
    db.commit()
    return db_user

@router.post('/update-password/{user_id}/{new_password}', response_model=UserSchema)
def update_password(user_id: int, new_password: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.BenutzerID == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.BenutzerPWD = new_password #TODO: Identitiy validation with old PWD
    db.commit()
    return db_user

@router.delete('/delete-user/{user_id}', response_model=UserSchema)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.BenutzerID == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return db_user