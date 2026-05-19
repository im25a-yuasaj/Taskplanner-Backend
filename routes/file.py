from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.file import File
from schemas.file import FileSchema, CreateFileSchema
from typing import List
import os

router = APIRouter(prefix="/file", tags=["file"])

@router.get('/', response_model=List[FileSchema])
def get_all_files(db: Session = Depends(get_db)):
    db_files = db.query(File).all()
    return db_files

@router.get('/{file_id}', response_model=FileSchema)
def get_file_by_id(file_id: int, db: Session = Depends(get_db)):
    db_file = db.query(File).filter(File.DateiID == file_id).first()
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    return db_file


@router.post('/create-file', response_model=FileSchema)
def create_file(file: CreateFileSchema, db: Session = Depends(get_db)):
    # Added check for file existence
    if not os.path.exists(file.Dateipfad):
        raise HTTPException(status_code=404, detail=f"File not found at path: {file.Dateipfad}")

    try:
        with open(file.Dateipfad, "rb") as f:
            file_data = f.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")

    db_file = File(
        AufgabeID=file.AufgabeID,
        Dateipfad=file.Dateipfad,
        DateiBLOB=file_data,
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

@router.post('/update-file/{file_id}/{new_directory}', response_model=FileSchema)
def update_file_directory(file_id: int, new_directory: str, db: Session = Depends(get_db)):
    db_file = db.query(File).filter(File.DateiID == file_id).first()
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    db_file.Dateipfad = new_directory
    db.commit()
    return db_file

@router.post('/update-file-blob/{file_id}/{new_blob}', response_model=FileSchema)
def update_file_blob(file_id: int, new_blob: str, db: Session = Depends(get_db)):
    db_file = db.query(File).filter(File.DateiID == file_id).first()
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    db_file.DateiBLOB = new_blob
    return db_file

@router.delete('/delete-file/{file_id}', response_model=FileSchema)
def delete_file(file_id: int, db: Session = Depends(get_db)):
    db_file = db.query(File).filter(File.DateiID == file_id).first()
    if db_file is None:
        raise HTTPException(status_code=404, detail="File not found")
    db.delete(db_file)
    db.commit()
    return db_file