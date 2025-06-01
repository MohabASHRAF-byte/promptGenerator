from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from backend.config.database import Base


class Instruction(Base):
    __tablename__ = "instructions"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    prompt_id = Column(Integer, ForeignKey("prompts.id"))
    prompt = relationship("Prompt", back_populates="instructions")
