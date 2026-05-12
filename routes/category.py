from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.category import Category
from schemas.category import CategorySchema, CreateCategorySchema
from typing import List

router = APIRouter(prefix='/category', tags=['category'])

@router.get('/', response_model=List[CategorySchema])
def get_all_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()


@router.get('/{kategorie_id}', response_model=CategorySchema)
def get_category_by_id(kategorie_id: int, db: Session = Depends(get_db)):
    db_category = (
        db.query(Category)
        .filter(Category.KategorieID == kategorie_id)
        .first()
    )

    if db_category is None:
        raise HTTPException(status_code=404, detail='Kategorie nicht gefunden')

    return db_category


@router.post('/create-category', response_model=CategorySchema)
def create_category(category: CreateCategorySchema, db: Session = Depends(get_db)):
    db_category = Category(
        Kategorie=category.Kategorie,
        IstAktiv=category.IstAktiv
    )

    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


@router.post('/update-category-name/{kategorie_id}/{new_name}', response_model=CategorySchema)
def update_category_name(kategorie_id: int, new_name: str, db: Session = Depends(get_db)):
    db_category = (
        db.query(Category)
        .filter(Category.KategorieID == kategorie_id)
        .first()
    )

    if db_category is None:
        raise HTTPException(status_code=404, detail='Kategorie nicht gefunden')

    db_category.Kategorie = new_name
    db.commit()
    db.refresh(db_category)

    return db_category


@router.post('/update-isactive/{kategorie_id}/{new_isactive}', response_model=CategorySchema)
def update_isactive(kategorie_id: int, new_isactive: bool, db: Session = Depends(get_db)):
    db_category = (
        db.query(Category)
        .filter(Category.KategorieID == kategorie_id)
        .first()
    )

    if db_category is None:
        raise HTTPException(status_code=404, detail='Kategorie nicht gefunden')

    db_category.IstAktiv = new_isactive
    db.commit()
    db.refresh(db_category)

    return db_category


@router.delete('/delete-category/{kategorie_id}', response_model=CategorySchema)
def delete_category(kategorie_id: int, db: Session = Depends(get_db)):
    db_category = (
        db.query(Category)
        .filter(Category.KategorieID == kategorie_id)
        .first()
    )

    if db_category is None:
        raise HTTPException(status_code=404, detail='Kategorie nicht gefunden')

    db.delete(db_category)
    db.commit()

    return db_category