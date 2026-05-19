'''
model for user
'''
from sqlalchemy import Column, Integer, String
from database.database import Base

class User(Base):
    __tablename__ = "benutzer"

    BenutzerID = Column(Integer, primary_key=True)
    BenutzerName = Column(String(255), unique=True)
    BenutzerPWD = Column(String(255))

    def __repr__(self):
        return f"<Benutzer {self.BenutzerName}>"