from typing import List, Optional

from pydantic import BaseModel


class PromptItem(BaseModel):
    name: str


class AddPrompt(BaseModel):
    project_id : int
    name : str
    code_only : bool


class UpdatePrompt(BaseModel):
    name : Optional[str]
    code_only : Optional[bool]


class GetPrompts(BaseModel):
    name : str
    description : str
    code_only : bool


class GetSinglePrompt(GetPrompts):
    instructions : List[str]
