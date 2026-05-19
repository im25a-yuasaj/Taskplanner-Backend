'''
model for tasks
'''
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
    KategorieID = Column(Integer, ForeignKey(Category.KategorieID))
    PrioritaetID = Column(Integer, ForeignKey(Priority.PrioritaetID))
    FortschrittID = Column(Integer, ForeignKey(Progress.FortschrittID))
    BenutzerID = Column(Integer, ForeignKey(User.BenutzerID))

    def __repr__(self):
        return f"<Aufgaben {self.Titel}>"

class TaskViewModel(Base):
    __tablename__ = "aufgaben_uebersicht"

    AufgabeID = Column(Integer, primary_key=True)
    Titel = Column(String(255))
    Ort = Column(String(255))
    Notiz = Column(TEXT)
    Kategorie = Column(String(255))
    Prioritaet = Column(String(255))
    Fortschritt = Column(String(255))
    BenutzerName = Column(String(255))
    Material = Column(String(255))