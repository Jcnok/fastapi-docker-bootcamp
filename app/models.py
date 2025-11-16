from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=100, description="Título da tarefa")
    description: Optional[str] = Field(None, max_length=500, description="Descrição detalhada")
    completed: bool = Field(default=False, description="Status de conclusão")
    created_at: Optional[datetime] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Aprender FastAPI",
                "description": "Completar o bootcamp de FastAPI com Docker",
                "completed": False
            }
        }