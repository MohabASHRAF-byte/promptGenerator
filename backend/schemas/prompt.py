from typing import List, Optional

from pydantic import BaseModel

from backend.schemas.instruction import InstructionBase


class PromptItem(BaseModel):
    name: str


class AddPrompt(BaseModel):
    project_id: int
    name: str
    code_only: bool


class UpdatePrompt(BaseModel):
    name: Optional[str]
    code_only: Optional[bool]


from pydantic import BaseModel


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

    @classmethod
    def from_orm_prompt(cls, prompt):
        return cls(
            id=prompt.id,
            name=prompt.name,
            code_only=prompt.code_only,
            numOfInstructions=len(prompt.instructions) if prompt.instructions else 0,
            instructions=[InstructionBase.from_Instruction_orm(ins) for ins in prompt.instructions]
        )


class GeneratePrompt(BaseModel):
    content: str


class GeneratePromptResponse(BaseModel):
    prompt: str
