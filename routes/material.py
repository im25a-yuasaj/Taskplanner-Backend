from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.material import Material
from schemas.material import MaterialSchema, CreateMaterialSchema
from typing import List

router = APIRouter(prefix='/material', tags=['material'])

@router.get('/', response_model=List[MaterialSchema])
def get_all_materials(db: Session = Depends(get_db)):
    return db.query(Material).all()


@router.get('/{material_id}', response_model=MaterialSchema)
def get_material_by_id(material_id: int, db: Session = Depends(get_db)):
    db_material = (
        db.query(Material)
        .filter(Material.MaterialID == material_id)
        .first()
    )

    if db_material is None:
        raise HTTPException(status_code=404, detail='Material nicht gefunden')

    return db_material


@router.post('/create-material', response_model=MaterialSchema)
def create_material(material: CreateMaterialSchema, db: Session = Depends(get_db)):
    db_material = Material(
        Material=material.Material,
        IstAktiv=material.IstAktiv
    )

    db.add(db_material)
    db.commit()
    db.refresh(db_material)

    return db_material


@router.post('/update-material-name/{material_id}/{new_name}', response_model=MaterialSchema)
def update_material_name(material_id: int, new_name: str, db: Session = Depends(get_db)):
    db_material = (
        db.query(Material)
        .filter(Material.MaterialID == material_id)
        .first()
    )

    if db_material is None:
        raise HTTPException(status_code=404, detail='Material nicht gefunden')

    db_material.Material = new_name
    db.commit()
    db.refresh(db_material)

    return db_material


@router.post('/update-isactive/{material_id}/{new_isactive}', response_model=MaterialSchema)
def update_isactive(material_id: int, new_isactive: bool, db: Session = Depends(get_db)):
    db_material = (
        db.query(Material)
        .filter(Material.MaterialID == material_id)
        .first()
    )

    if db_material is None:
        raise HTTPException(status_code=404, detail='Material nicht gefunden')

    db_material.IstAktiv = new_isactive
    db.commit()
    db.refresh(db_material)

    return db_material


@router.delete('/delete-material/{material_id}', response_model=MaterialSchema)
def delete_material(material_id: int, db: Session = Depends(get_db)):
    db_material = (
        db.query(Material)
        .filter(Material.MaterialID == material_id)
        .first()
    )

    if db_material is None:
        raise HTTPException(status_code=404, detail='Material nicht gefunden')

    db.delete(db_material)
    db.commit()

    return db_material