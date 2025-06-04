from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.schemas.prompt import AddPrompt, GetPrompts, UpdatePrompt, GeneratePrompt
from backend.services.promptService import add_new_prompt_service, update_prompt_service, delete_prompt_service, \
    get_prompts_service, get_single_prompt_service, generate_prompt_service

router = APIRouter(prefix="/prompts", tags=["prompts"])


@router.post("/")
def add_new_prompt(prompt: AddPrompt, db: Session = Depends(get_db)):
    return add_new_prompt_service(prompt, db)


@router.get("/{pid}")
def get_single_prompt(
        pid: int,
        db: Session = Depends(get_db)
):
    return get_single_prompt_service(pid, db)


@router.get("/", response_model=List[GetPrompts])
def get_prompts(
        projectId: int,
        db: Session = Depends(get_db)
):
    return get_prompts_service(projectId, db)


@router.put("/{pid}")
def update_prompt(
        pid: int,
        prompt: UpdatePrompt,
        db: Session = Depends(get_db)
):
    return update_prompt_service(pid, prompt, db)


@router.delete("/{pid}")
def delete_prompt(
        pid: int,
        db: Session = Depends(get_db)
):
    return delete_prompt_service(pid, db)




@router.post("/{pid}/generate")
def generate_prompt(
        pid: int,
        prompt : GeneratePrompt,
        db: Session = Depends(get_db)
):
    return {"data":generate_prompt_service(pid,prompt,db)}
