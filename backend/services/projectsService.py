from typing import List

from sqlalchemy.orm import Session, joinedload
from starlette.exceptions import HTTPException

from backend.models.projects import Project
from backend.schemas.project import ProjectCreate, GetProjectsItem, UpdateProject, GetSingleProject


def add_new_project_service(project: ProjectCreate, db: Session):
    project = Project(name=project.name, description=project.description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_all_projects(db: Session) -> List[GetProjectsItem]:
    # Eagerly load the prompts relationship
    projects = db.query(Project).options(joinedload(Project.prompts)).all()
    ret_projects = []
    for proj in projects:
        ret_projects.append(GetProjectsItem(
            description=proj.description,
            name=proj.name,
            numberOfItems=len(proj.prompts),  # No need for conditional check
            id=proj.id
        ))
    return ret_projects


def get_project_service(id: int, db: Session):
    db_project = (
        db.query(Project)
        .options(joinedload(Project.prompts))
        .filter(Project.id == id)
        .first()
    )
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return GetSingleProject.from_orm_project(db_project)


def update_project_service(id: int, project: UpdateProject, db: Session):
    db_project = get_project_service(id, db)
    if project.name is not None:
        db_project.name = project.name
    if project.description is not None:
        db_project.description = project.description

    db.commit()
    db.refresh(db_project)
    return db_project


def delete_project_service(id: int, db: Session):
    db_project = get_project_service(id, db)
    db.delete(db_project)
    db.commit()
    return {"message": "Deleted successfully "}
