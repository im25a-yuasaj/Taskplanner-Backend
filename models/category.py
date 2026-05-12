from sqlalchemy import Column, Integer, String
from database.database import Base

class Category(Base):
    __tablename__ = "Category"

    CategoryID = Column(Integer, primary_key=True)
    Category = Column(String(255), unique=True)
    IsActive = Boolean, default=True

    def __repr__(self):
        return f"<Category {self.Category}>"