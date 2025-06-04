from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from backend.config.database import Base

class Prompt(Base):
    __tablename__ = "prompts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code_only = Column(Boolean, default=False)
    ai_role = Column(String, default=None)
    experience_level = Column(String, default="expert")
    is_code = Column(Boolean, default=False)
    project_id = Column(Integer, ForeignKey("projects.id"))
    project = relationship("Project", back_populates="prompts")
    instructions = relationship(
        "Instruction",
        back_populates="prompt",
        cascade="all, delete-orphan"
    )
