from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.config.database import get_db
from backend.models.prompt import Prompt

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("/test-connection")
def test_database_connection(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")  # Simple query to test connection
        return {"status": "success", "message": "Database connection successful!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {e}")


@router.post("/test-insert")
def test_database_insert(db: Session = Depends(get_db)):
    try:
        db_project = Prompt(name="hdfd")
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return {"status": "success", "message": "Inserted dummy project!", "project_id": db_project.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database insert failed: {e}")


@router.get("/prompts")
def get_all_prompts(db: Session = Depends(get_db)):
    try:
        prompts = db.query(Prompt).all()
        return prompts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not fetch prompts: {e}")
