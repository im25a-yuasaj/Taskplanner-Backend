'''
model for files
'''
from sqlalchemy import Column, Integer, String, BLOB, ForeignKey
from database.database import Base
from models.task import Task

class File(Base):
    __tablename__ = "Datei"

    DateiID = Column(Integer, primary_key=True)
    AufgabeID = Column(Integer, ForeignKey(Task.AufgabeID))
    Dateipfad = Column(String(255))
    DateiBLOB = Column(BLOB)