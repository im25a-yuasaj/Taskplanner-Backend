from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.taskmaterial import TaskMaterial
from schemas.taskmaterial import TaskMaterialSchema, CreateTaskMaterialSchema
from typing import List

router = APIRouter(prefix='/task-material', tags=['task-material'])

@router.get('/', response_model=List[TaskMaterialSchema])
def get_all_taskmaterials(db: Session = Depends(get_db)):
    return db.query(TaskMaterial).all()

@router.get('/{aufgabe_id}/{material_id}', response_model=TaskMaterialSchema)
def get_taskmaterial_by_id(aufgabe_id: int, material_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(TaskMaterial).filter(
        TaskMaterial.AufgabeID == aufgabe_id,
        TaskMaterial.MaterialID == material_id
    ).first()
    if db_entry is None:
        raise HTTPException(status_code=404, detail='TaskMaterial not found')
    return db_entry

@router.post('/create/{aufgabe_id}/{material_id}', response_model=TaskMaterialSchema)
def create_taskmaterial(aufgabe_id: int, material_id: int, body: CreateTaskMaterialSchema, db: Session = Depends(get_db)):
    db_entry = TaskMaterial(
        AufgabeID=aufgabe_id,
        MaterialID=material_id,
        Anzahl=body.Anzahl,
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.delete('/delete/{aufgabe_id}/{material_id}', response_model=TaskMaterialSchema)
def delete_taskmaterial(aufgabe_id: int, material_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(TaskMaterial).filter(
        TaskMaterial.AufgabeID == aufgabe_id,
        TaskMaterial.MaterialID == material_id
    ).first()
    if db_entry is None:
        raise HTTPException(status_code=404, detail='TaskMaterial not found')
    db.delete(db_entry)
    db.commit()
    return db_entry