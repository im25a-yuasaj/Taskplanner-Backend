from sqlalchemy import Column, Integer, String
from database.database import Base

class User(Base):
    __tablename__ = "benutzer"

    UserID = Column(Integer, primary_key=True)
    UserName = Column(String(255), unique=True)
    UserPWD = Column(String(255))

    def __repr__(self):
        return f"<Benutzer {self.UserName}>"