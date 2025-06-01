from typing import List, Optional, Self

from pydantic import BaseModel

from backend.models.projects import Project
from backend.schemas.prompt import PromptItem, GetPrompts


class ProjectBase(BaseModel):
    name: str


class ProjectCreate(ProjectBase):
    name: str
    description: str


class GetProjectsItem(BaseModel):
    id: int
    name: str
    description: str
    numberOfItems: int


class GetSingleProject(GetProjectsItem):
    prompts: List[GetPrompts]

    @classmethod
    def from_orm_project(cls, proj: Project) -> Self:
        return cls(
            id=proj.id,
            name=proj.name,
            description=proj.description,
            numberOfItems=len(proj.prompts) if proj.prompts else 0,
            prompts=[GetPrompts.from_orm_prompt(prompt) for prompt in proj.prompts],

        )


class ProjectResponse(ProjectBase):
    id: int
    user_id: int


class UpdateProject(BaseModel):
    name: Optional[str]
    description: Optional[str]


class ProjectWithRecordsResponse(BaseModel):
    project: ProjectResponse
    records: List[PromptItem]
