from sqlalchemy import Column, Integer, String, DATETIME, TEXT, ForeignKey
from database.database import Base
from models.category import Category
from models.priority import Priority
from models.progress import Progress
from models.user import User

class Task(Base):
    __tablename__ = "aufgabe"

    AufgabeID = Column(Integer, primary_key=True)
    Titel = Column(String(255))
    Beginn = Column(DATETIME)
    Ende = Column(DATETIME)
    Ort = Column(String(255))
    Koordinaten = Column(String(255))
    Notiz = Column(TEXT)

    def __repr__(self):
        return f"<Aufgaben {self.Titel}>"