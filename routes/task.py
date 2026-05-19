from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.task import Task
from schemas.task import TaskSchema, CreateTaskSchema
from typing import List


router = APIRouter(prefix="/task", tags=["task"])

@router.get('/', response_model=List[TaskSchema])
def get_all_tasks(db: Session = Depends(get_db)):
    db_tasks = db.query(Task).all()
    return db_tasks

@router.get('/{task_id}', response_model=TaskSchema)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.AufgabeID == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_task

@router.post('/create-task', response_model=TaskSchema)
def create_task(user: CreateTaskSchema, db: Session = Depends(get_db)):
    db_user = Task(
        Titel=user.Titel,
        Beginn=user.Beginn,
        Ende=user.Ende,
        Ort=user.Ort,
        Koordinaten=user.Koordinaten,
        Notiz=user.Notiz,
        KategorieID=user.KategorieID,
        PrioritaetID=user.PrioritaetID,
        FortschrittID=user.FortschrittID,
        BenutzerID=user.BenutzerID,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete('/delete-user/{task_id}', response_model=TaskSchema)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.BenutzerID == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_task)
    db.commit()
    return db_task