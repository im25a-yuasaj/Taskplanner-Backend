from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base

class Material(Base):
    __tablename__ = 'Material'

    MaterialID = Column(Integer, primary_key=True, autoincrement=True)
    Material = Column(String(100), nullable=False)
    IstAktiv = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Category {self.Kategorie}>'