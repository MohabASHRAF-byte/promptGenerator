from typing import Optional, Any, Self

from pydantic import BaseModel

from backend.models.instruction import Instruction


class InstructionBase(BaseModel):
    id: int
    content: str
    @classmethod
    def from_Instruction_orm(cls, instruction: Instruction) -> Self:
        return cls(
            id = instruction.id,
            content= instruction.content
        )

class InstructionCreate(BaseModel):
    promptId: int
    content: str


class InstructionUpdate(BaseModel):
    content: Optional[str]
