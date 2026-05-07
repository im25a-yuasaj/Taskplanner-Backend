from fastapi import APIRouter, Depends
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