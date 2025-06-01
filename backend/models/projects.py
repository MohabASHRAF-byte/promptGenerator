from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from backend.config.database import Base


class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text, default="")
    prompts = relationship("Prompt", back_populates="project", cascade="all, delete-orphan")
