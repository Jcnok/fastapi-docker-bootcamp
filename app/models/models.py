from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional
from datetime import datetime

TITLE_MAX = 100
DESC_MAX = 500

class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=TITLE_MAX, description="Título da tarefa")
    description: Optional[str] = Field(None, max_length=DESC_MAX, description="Descrição detalhada")
    completed: bool = Field(default=False, description="Status de conclusão")
    created_at: Optional[datetime] = None


    @field_validator('title')
    @classmethod
    def strip_title(cls, title: str) -> str:
        title = title.strip()
        if not title:
            raise ValueError('Título não pode ser vazio ou apenas espaços')
        return title

   
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "title": "Aprender FastAPI",
                "description": "Completar o bootcamp de FastAPI com Docker",
                "completed": False
            }
        }
    )