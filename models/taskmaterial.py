from sqlalchemy import Column, Integer, ForeignKey
from database.database import Base
from models.task import Task
from models.material import Material

class TaskMaterial(Base):
    __tablename__ = "AufgabeMaterial"

    AufgabeID = Column(Integer, primary_key=True)
    MaterialID = Column(Integer, primary_key=True)
    Anzahl = Column(Integer)
    ForeignKey(Task.AufgabeID)
    ForeignKey(Material.MaterialID)

    def __repr__(self):
        return f"<Aufgabe Material {self.AufgabeID}>"