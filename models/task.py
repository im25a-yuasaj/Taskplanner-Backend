from sqlalchemy import Column, Integer, String, DATETIME, TEXT, ForeignKey
from database.database import Base
from category import Category
from priority import Priority
from progress import Progress
from user import User


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