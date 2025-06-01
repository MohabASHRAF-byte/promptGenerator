from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.schemas.project import ProjectCreate, GetProjectsItem, UpdateProject
from backend.services.projectsService import add_new_project_service, get_all_projects, update_project_service

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/")
def add_new_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return add_new_project_service(project, db)


@router.get("/", response_model=List[GetProjectsItem])
def get_projects(db: Session = Depends(get_db)):
    return get_all_projects(db)


from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from backend.config.database import get_db

@router.put("/{id}")
def update_project(
    id: int,
    project: UpdateProject,
    db: Session = Depends(get_db)
):
    return update_project_service(id, project, db)
