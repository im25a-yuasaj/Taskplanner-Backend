from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.progress import Progress
from schemas.progress import ProgressSchema
from typing import List

router = APIRouter(prefix="/progress", tags=["progress"])


@router.get('/', response_model=List[ProgressSchema])
def get_all_users(db: Session = Depends(get_db)):
    db_users = db.query(Progress).all()
    return db_users

@router.get('/{user_id}', response_model=ProgressSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(Progress).filter(Progress.BenutzerID == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user