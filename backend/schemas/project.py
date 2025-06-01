from typing import List, Optional

from pydantic import BaseModel

from backend.schemas.prompt import PromptItem


class ProjectBase(BaseModel):
    name: str


class ProjectCreate(ProjectBase):
    name: str
    description: str


class GetProjectsItem(ProjectCreate):
    id: int
    name: str
    description: str
    numberOfItems: int


class ProjectResponse(ProjectBase):
    id: int
    user_id: int


class UpdateProject(BaseModel):
    name: Optional[str]
    description: Optional[str]


class ProjectWithRecordsResponse(BaseModel):
    project: ProjectResponse
    records: List[PromptItem]
