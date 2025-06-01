from typing import Optional

from pydantic import BaseModel


class InstructionCreate(BaseModel):
    promptId: int
    content: str


class InstructionUpdate(BaseModel):
    content: Optional[str]
