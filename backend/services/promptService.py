from sqlalchemy.orm import Session, joinedload
from starlette.exceptions import HTTPException

from backend.Ai_Model.ChatGPT import ChatGPT
from backend.models.prompt import Prompt
from backend.schemas.prompt import AddPrompt, UpdatePrompt, GetSinglePrompt, GeneratePrompt
from backend.services.projectsService import get_project_service


def add_new_prompt_service(prompt: AddPrompt, db: Session):
    project = get_project_service(prompt.project_id, db)
    prom = Prompt(name=prompt.name, code_only=prompt.code_only, project=project)
    db.add(prom)
    db.commit()
    db.refresh(prom)
    return prom


def get_single_prompt_service(pid: int, db: Session):
    db_prompt = (
        db.query(Prompt)
        .options(joinedload(Prompt.instructions))
        .filter(Prompt.id == pid)
        .first()
    )
    if not db_prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return GetSinglePrompt.from_orm_prompt(db_prompt)


def _get_single_prompt_service(pid: int, db: Session):
    db_project = db.query(Prompt).filter(pid == Prompt.id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="prompt not found")
    return db_project


def get_prompts_service(projectId: int, db: Session):
    db_projects = db.query(Prompt).filter(projectId == Prompt.project_id).all()
    return db_projects


def update_prompt_service(pid: int, prompt: UpdatePrompt, db: Session):
    project = _get_single_prompt_service(pid, db)
    if prompt.code_only:
        project.code_only = prompt.code_only
    if prompt.name:
        project.name = prompt.name
    db.commit()
    db.refresh(project)
    return project


def delete_prompt_service(pid: int, db: Session):
    project = _get_single_prompt_service(pid, db)
    db.delete(project)
    db.commit()
    return {"message": "Deleted successfully "}


def generate_prompt_service(pid: int, genPrompt: GeneratePrompt, db: Session):
    prompt = get_single_prompt_service(pid, db)
    ins = [ins.content for ins in prompt.instructions]
    chat_gpt = ChatGPT()
    task = chat_gpt.generate_prompt(
        ins,
        genPrompt.content,
        output_only_code=True
    )
    return task
