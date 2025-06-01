from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.schemas.instruction import InstructionCreate, InstructionUpdate
from backend.services.instuctionService import add_new_instruction_service, update_instruction_service, \
    delete_instruction_service

router = APIRouter(prefix="/instruction", tags=["instructions"])


@router.post("/")
def add_new_instruction(ins: InstructionCreate, db: Session = Depends(get_db)):
    return add_new_instruction_service(ins, db)


@router.put("/{iid}")
def update_project(
        iid: int,
        project: InstructionUpdate,
        db: Session = Depends(get_db)
):
    return update_instruction_service(iid, project, db)


@router.delete("/{iid")
def delete_project(
        iid: int,
        db: Session = Depends(get_db)
):
    return delete_instruction_service(iid, db)
