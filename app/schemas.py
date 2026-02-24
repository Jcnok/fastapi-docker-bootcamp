# app/schemas.py

from pydantic import BaseModel, Field
from typing import Optional

# Modelo para atualização parcial de uma Tarefa
class TaskUpdatePartial(BaseModel):
    """Permite enviar APENAS os campos que serão alterados."""
    title: Optional[str] = Field(None, description="Opcional. Novo título da tarefa.")
    description: Optional[str] = Field(None, description="Opcional. Nova descrição da tarefa.")
    completed: Optional[bool] = Field(None, description="Opcional. Novo status de conclusão (True/False).")
    # Se você tiver outros campos (ex: due_date), adicione-os aqui como Optional[Tipo]
    
    class Config:
        # Garante que campos não definidos não sejam enviados
        extra = "forbid"