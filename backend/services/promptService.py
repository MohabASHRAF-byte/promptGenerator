from sqlalchemy.orm import Session, joinedload
from starlette.exceptions import HTTPException

from backend.Ai_Model.ChatGPT import ChatGPT
from backend.models.prompt import Prompt
from backend.schemas.prompt import AddPrompt, UpdatePrompt, GetSinglePrompt, GeneratePrompt, GeneratePromptResponse
from backend.services.projectsService import get_project_service


def add_new_prompt_service(prompt: AddPrompt, db: Session):
    # Use prompt.project_id, not cls.project_id
    print(prompt.project_id)
    get_project_service(prompt.project_id, db)
    prom = prompt.to_prompt()  # No need for print(cls.project_id) here
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


def _get_single_prompt_service(pid: int, db: Session) -> Prompt:
    db_project = db.query(Prompt).filter(pid == Prompt.id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="prompt not found")
    return db_project


def get_prompts_service(projectId: int, db: Session):
    db_projects = db.query(Prompt).filter(projectId == Prompt.project_id).all()
    return db_projects


def update_prompt_service(pid: int, prompt: UpdatePrompt, db: Session):
    prom = _get_single_prompt_service(pid, db)
    for org_attrname, org_value in vars(prom).items():
        for updt_attrname, updt_value in vars(prompt).items():
            if org_attrname == updt_attrname:
                if updt_value is None:
                    continue
                setattr(prom, org_attrname, updt_value)
    db.commit()
    db.refresh(prom)
    return prom


def delete_prompt_service(pid: int, db: Session):
    project = _get_single_prompt_service(pid, db)
    db.delete(project)
    db.commit()
    return {"message": "Deleted successfully "}


def generate_prompt_service(pid: int, genPrompt: GeneratePrompt, db: Session):
    prompt = get_single_prompt_service(pid, db)
    project = get_project_service(prompt.project_id, db)
    ins = [ins.content for ins in prompt.instructions]
    chat_gpt = ChatGPT()
    task = chat_gpt.generate_prompt_message(
        ai_role=prompt.ai_role,
        experience_level=prompt.experience_level,
        prompt_query_text=genPrompt.content,
        instructions=ins,
        output_only_code=prompt.code_only,
        project_description=project.description
    )
    response = GeneratePromptResponse(
        prompt=task
    )
    return response
