from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.schemas.project import ProjectCreate, GetProjectsItem, UpdateProject
from backend.services.projectsService import add_new_project_service, get_all_projects, update_project_service, \
    get_project_service, delete_project_service

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/")
def add_new_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return add_new_project_service(project, db)


@router.get("/{pid}")
def get_single_project(
        pid: int,
        db: Session = Depends(get_db)
):
    return get_project_service(pid, db)


@router.get("/", response_model=List[GetProjectsItem])
def get_projects(db: Session = Depends(get_db)):
    return get_all_projects(db)


@router.put("/{pid}")
def update_project(
        pid: int,
        project: UpdateProject,
        db: Session = Depends(get_db)
):
    return update_project_service(pid, project, db)


@router.delete("/{pid")
def delete_project(
        pid: int,
        db: Session = Depends(get_db)
):
    return delete_project_service(pid, db)
