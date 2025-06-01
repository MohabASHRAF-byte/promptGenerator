from typing import List, Optional

from pydantic import BaseModel


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
    instructions: List[str]
