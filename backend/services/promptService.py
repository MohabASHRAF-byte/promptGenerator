from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from backend.models.prompt import Prompt
from backend.schemas.prompt import AddPrompt, UpdatePrompt
from backend.services.projectsService import get_project_service


def add_new_prompt_service(prompt: AddPrompt, db: Session):
    project = get_project_service(prompt.project_id, db)
    prom = Prompt(name=prompt.name, code_only=prompt.code_only, project=project)
    db.add(prom)
    db.commit()
    db.refresh(prom)
    return prom


def get_single_prompt_service(pid: int, db: Session):
    db_project = db.query(Prompt).filter(pid == Prompt.id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="prompt not found")
    return db_project


def get_prompts_service(projectId: int, db: Session):
    db_projects = db.query(Prompt).filter(projectId == Prompt.project_id).all()
    return db_projects


def update_prompt_service(pid: int, prompt: UpdatePrompt, db: Session):
    project = get_single_prompt_service(pid, db)
    if prompt.code_only:
        project.code_only = prompt.code_only
    if prompt.name:
        project.name = prompt.name
    db.commit()
    db.refresh(project)
    return project


def delete_prompt_service(pid: int, db: Session):
    project = get_single_prompt_service(pid, db)
    db.delete(project)
    db.commit()
    return {"message": "Deleted successfully "}
