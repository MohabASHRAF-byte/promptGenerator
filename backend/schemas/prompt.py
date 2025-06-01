from pydantic import BaseModel


class PromptItem(BaseModel):
    name: str
