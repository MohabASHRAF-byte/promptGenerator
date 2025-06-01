from typing import List

from pydantic import BaseModel

from backend.schemas.prompt import PromptItem


class ProjectBase(BaseModel):
    name: str


class ProjectCreate(ProjectBase):
    name: str
    description: str


class GetProjectsItem(ProjectCreate):
    id: int
    numberOfItems: int


class ProjectResponse(ProjectBase):
    id: int
    user_id: int


class ProjectWithRecordsResponse(BaseModel):
    project: ProjectResponse
    records: List[PromptItem]
