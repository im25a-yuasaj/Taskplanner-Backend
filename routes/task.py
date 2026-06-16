'''
routes for task table
'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.task import Task, TaskViewModel
from schemas.task import TaskSchema, CreateTaskSchema, TaskViewSchema
from typing import List


router = APIRouter(prefix="/task", tags=["task"])

@router.get('/', response_model=List[TaskSchema])
def get_all_tasks(db: Session = Depends(get_db)):
    db_tasks = db.query(Task).all()
    return db_tasks
@router.get('/get-task-views', response_model=List[TaskViewSchema])
def get_task_views(db: Session = Depends(get_db)):
    db_task_view = db.query(TaskViewModel).all()
    return db_task_view

@router.get('/{task_id}', response_model=TaskSchema)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.AufgabeID == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    return db_task


@router.post('/create-task', response_model=TaskSchema)
def create_task(task: CreateTaskSchema, db: Session = Depends(get_db)):
    db_task = Task(
        Titel=task.Titel,
        Beginn=task.Beginn,
        Ende=task.Ende,
        Ort=task.Ort,
        Koordinaten=task.Koordinaten,
        Notiz=task.Notiz,
        KategorieID=task.KategorieID,
        PrioritaetID=task.PrioritaetID,
        FortschrittID=task.FortschrittID,
        BenutzerID=task.BenutzerID,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.post('/update-task/{task_id}/{new_name}', response_model=TaskSchema)
def update_taskname(task_id: int, new_name: str, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.AufgabeID == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    db_task.Titel = new_name
    db.commit()
    return db_task

@router.post('/update-task-status/{task_id}/{new_status}', response_model=TaskSchema)
def update_taskname(task_id: int, new_status: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.AufgabeID == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    db_task.FortschrittID = new_status
    db.commit()
    return db_task

@router.post('/update-task-note/{task_id}/{new_note}', response_model=TaskSchema)
def update_task_note(task_id: int, new_note: str, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.AufgabeID == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    db_task.Notiz = new_note
    db.commit()
    return db_task

@router.delete('/delete-task/{task_id}', response_model=TaskSchema)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.AufgabeID == task_id).first()
    if db_task is None:
        raise HTTPException(status_code=404, detail="task not found")
    db.delete(db_task)
    db.commit()
    return db_task