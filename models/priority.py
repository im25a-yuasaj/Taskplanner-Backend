from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base

class Priority(Base):
    __tablename__ = 'Prioritaet'

    PrioritaetID = Column(Integer, primary_key=True, autoincrement=True)
    Prioritaet = Column(String(100), nullable=False)

    def __repr__(self):
        return f'<Category {self.Prioritaet}>'