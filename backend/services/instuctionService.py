from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from backend.models.instruction import Instruction
from backend.schemas.instruction import InstructionCreate, InstructionUpdate
from backend.services.promptService import _get_single_prompt_service


def add_new_instruction_service(instruction: InstructionCreate, db: Session):
    prompt = _get_single_prompt_service(instruction.promptId, db)
    ins = Instruction(content=instruction.content, prompt=prompt)
    db.add(ins)
    db.commit()
    db.refresh(ins)
    return ins


def get_single_instruction_service(iid: int, db: Session):
    db_instruction = db.query(Instruction).filter(iid == Instruction.id).first()
    if not db_instruction:
        raise HTTPException(status_code=404, detail="instruction not found")
    return db_instruction


def update_instruction_service(iid: int, inst: InstructionUpdate, db: Session):
    ins = get_single_instruction_service(iid, db)
    if inst.content:
        ins.content = inst.content
    db.commit()
    db.refresh(ins)
    return ins


def delete_instruction_service(iid: int, db: Session):
    ins = get_single_instruction_service(iid, db)
    db.delete(ins)
    db.commit()
    return {"message": "Deleted successfully "}
