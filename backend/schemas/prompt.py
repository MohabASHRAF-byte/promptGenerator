from typing import List, Optional, Type

from pydantic import BaseModel

from backend.models.prompt import Prompt
from backend.schemas.instruction import InstructionBase


class PromptItem(BaseModel):
    name: str

class AddPrompt(BaseModel):
    project_id: int
    name: str
    code_only: bool
    ai_role: Optional[str] = None
    experience_level: str = "Expert"
    is_code: bool = False

    def to_prompt(self) -> Prompt:
        return Prompt(
            project_id=self.project_id,
            name=self.name,
            code_only=self.code_only,
            ai_role=self.ai_role,
            experience_level=self.experience_level or "Expert",
            is_code=self.is_code or False
        )

class UpdatePrompt(BaseModel):
    name: Optional[str] = None
    code_only: Optional[bool] = None
    ai_role: Optional[str] = None
    experience_level: Optional[str] = None
    is_code: Optional[bool] = None


class GetPrompts(BaseModel):
    id: int
    name: str
    code_only: bool

    @classmethod
    def from_orm_prompt(cls, prompt):
        return cls(
            id=prompt.id,
            name=prompt.name,
            code_only=prompt.code_only
        )

    class Config:
        orm_mode = True


class GetSinglePrompt(GetPrompts):
    numOfInstructions: int
    instructions: List[InstructionBase]
    ai_role: str
    experience_level: str = "Expert"
    ai_role: Optional[str]
    experience_level: str
    is_code: Optional[bool]
    project_id:int
    @classmethod
    def from_orm_prompt(cls, prompt):
        return cls(
            id=prompt.id,
            name=prompt.name,
            code_only=prompt.code_only,
            numOfInstructions=len(prompt.instructions) if prompt.instructions else 0,
            instructions=[InstructionBase.from_Instruction_orm(ins) for ins in prompt.instructions],
            ai_role=prompt.ai_role,
            experience_level=prompt.experience_level,
            is_code=prompt.is_code,
            project_id=prompt.project_id
        )


class GeneratePrompt(BaseModel):
    content: str


class GeneratePromptResponse(BaseModel):
    prompt: str
