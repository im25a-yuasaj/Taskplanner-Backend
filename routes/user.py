from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.database import get_db
from models.user import User
from schemas.user import UserSchema
from typing import List

router = APIRouter(prefix="/user", tags=["user"])

@router.get('/', response_model=List[UserSchema])
def get_all_users(db: Session = Depends(get_db)):
    db_users = db.query(User).all()
    return db_users