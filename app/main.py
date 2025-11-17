from fastapi import FastAPI, HTTPException, status
from typing import List
from app.models import Task
from app import database

app = FastAPI(
    title="To-Do List API",
    description="API simples para gerenciar tarefas",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
def read_root():
    """Endpoint raiz da API"""
    return {
        "message": "Bem-vindo à To-Do List API!",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# CREATE - Criar nova tarefa
@app.post(
    "/tasks/",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
    tags=["Tasks"]
)
def create_task(task: Task):
    """Cria uma nova tarefa"""
    return database.create_task(task)

# READ - Listar todas as tarefas
@app.get(
    "/tasks/",
    response_model=List[Task],
    tags=["Tasks"]
)
def get_tasks():
    """Lista todas as tarefas"""
    return database.get_all_tasks()

# READ - Buscar tarefa específica por ID
@app.get(
    "/tasks/{task_id}",
    response_model=Task,
    tags=["Tasks"]
)
def get_task(task_id: int):
    """Busca uma tarefa específica por ID"""
    task = database.get_task_by_id(task_id)
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return task

# UPDATE - Atualizar tarefa existente
@app.put(
    "/tasks/{task_id}",
    response_model=Task,
    tags=["Tasks"]
)
def update_task(task_id: int, task: Task):
    """Atualiza uma tarefa existente"""
    updated = database.update_task(task_id, task)
    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return updated

# DELETE - Remover tarefa
@app.delete(
    "/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Tasks"]
)
def delete_task(task_id: int):
    """Remove uma tarefa"""
    deleted = database.delete_task(task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tarefa com ID {task_id} não encontrada"
        )
    return None