'''
routes for progress
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.progress import Progress
from schemas.progress import ProgressSchema, CreateProgressSchema
from typing import List

router = APIRouter(prefix="/progress", tags=["progress"])


@router.get('/', response_model=List[ProgressSchema])
def get_all_progresss(db: Session = Depends(get_db)):
    db_progress = db.query(Progress).all()
    return db_progress

@router.get('/{progress_id}', response_model=ProgressSchema)
def get_progress_by_id(progress_id: int, db: Session = Depends(get_db)):
    db_progress = db.query(Progress).filter(Progress.FortschrittID == progress_id).first()
    if db_progress is None:
        raise HTTPException(status_code=404, detail="progress not found")
    return db_progress

@router.post('/create-progress', response_model=ProgressSchema)
def create_progress(progress: CreateProgressSchema, db: Session = Depends(get_db)):
    db_progress = Progress(
        Fortschritt=progress.Fortschritt,
    )
    db.add(db_progress)
    db.commit()
    db.refresh(db_progress)
    return db_progress

@router.post('/update-progress/{progress_id}/{new_progress}', response_model=ProgressSchema)
def update_progressname(progress_id: int, new_progress: str, db: Session = Depends(get_db)):
    db_progress = db.query(Progress).filter(Progress.FortschrittID == progress_id).first()
    if db_progress is None:
        raise HTTPException(status_code=404, detail="progress not found")
    db_progress.Fortschritt = new_progress
    db.commit()
    return db_progress

@router.delete('/delete-progress/{progress_id}', response_model=ProgressSchema)
def delete_progress(progress_id: int, db: Session = Depends(get_db)):
    db_progress = db.query(Progress).filter(Progress.FortschrittID == progress_id).first()
    if db_progress is None:
        raise HTTPException(status_code=404, detail="progress not found")
    db.delete(db_progress)
    db.commit()
    return db_progres