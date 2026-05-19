'''
model for progress
'''
from sqlalchemy import Column, Integer, String
from database.database import Base

class Progress(Base):
    __tablename__ = "fortschritt"

    FortschrittID = Column(Integer, primary_key=True)
    Fortschritt = Column(String(100))


    def __repr__(self):
        return f"<Benutzer {self.Fortschritt}>"