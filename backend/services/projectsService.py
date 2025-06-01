from typing import List

from sqlalchemy.orm import Session

from backend.models.projects import Project
from backend.schemas.project import ProjectCreate, GetProjectsItem


def add_new_project_service(project: ProjectCreate, db: Session):
    project = Project(name=project.name, description=project.description)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

from sqlalchemy.orm import joinedload
from typing import List

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