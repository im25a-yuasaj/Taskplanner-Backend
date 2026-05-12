from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base

class Category(Base):
    __tablename__ = 'Kategorie'

    KategorieID = Column(Integer, primary_key=True, autoincrement=True)
    Kategorie = Column(String(100), nullable=False)
    IstAktiv = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Category {self.Kategorie}>'