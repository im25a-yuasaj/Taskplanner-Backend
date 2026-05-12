from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.priority import Priority
from schemas.priority import PrioritySchema, CreatePrioritySchema
from typing import List

router = APIRouter(prefix='/priority', tags=['priority'])

@router.get('/', response_model=List[PrioritySchema])
def get_all_priorities(db: Session = Depends(get_db)):
    return db.query(Priority).all()


@router.get('/{Prioritaet_id}', response_model=PrioritySchema)
def get_category_by_id(prioritaet_id: int, db: Session = Depends(get_db)):
    db_priority = (
        db.query(Priority)
        .filter(Priority.PrioritaetID == prioritaet_id)
        .first()
    )

    if db_priority is None:
        raise HTTPException(status_code=404, detail='Priorität nicht gefunden')

    return db_priority


@router.post('/create-priority', response_model=PrioritySchema)
def create_priority(priority: CreatePrioritySchema, db: Session = Depends(get_db)):
    db_priority = Priority(
        Prioritaet=priority.Prioritaet,
    )

    db.add(db_priority)
    db.commit()
    db.refresh(db_priority)

    return db_priority


@router.post('/update-priority-name/{prioritaet_id}/{new_name}', response_model=PrioritySchema)
def update_priority_name(prioritaet_id: int, new_name: str, db: Session = Depends(get_db)):
    db_priority = (
        db.query(Priority)
        .filter(Priority.PrioritaetID == prioritaet_id)
        .first()
    )

    if db_priority is None:
        raise HTTPException(status_code=404, detail='Priorität nicht gefunden')

    db_priority.Prioritaet = new_name
    db.commit()
    db.refresh(db_priority)

    return db_priority


@router.delete('/delete-priority/{prioritaet_id}', response_model=PrioritySchema)
def delete_priority(prioritaet_id: int, db: Session = Depends(get_db)):
    db_priority = (
        db.query(Priority)
        .filter(Priority.PrioritaetID == prioritaet_id)
        .first()
    )

    if db_priority is None:
        raise HTTPException(status_code=404, detail='Priorität nicht gefunden')

    db.delete(db_priority)
    db.commit()

    return db_priority