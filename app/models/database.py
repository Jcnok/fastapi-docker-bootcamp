from typing import List, Optional
from app.models.models import Task
from datetime import datetime

# Simulando um banco de dados com lista em memória
tasks_db: List[Task] = []
next_id = 1

def get_next_id() -> int:
    """Gera o próximo ID único para tarefa"""
    global next_id
    current_id = next_id
    next_id += 1
    return current_id

def create_task(task: Task) -> Task:
    """Cria uma nova tarefa no banco"""
    task.id = get_next_id()
    task.created_at = datetime.now()
    tasks_db.append(task)
    return task

def get_all_tasks() -> List[Task]:
    """Retorna todas as tarefas"""
    return tasks_db

def get_task_by_id(task_id: int) -> Optional[Task]:
    """Busca uma tarefa por ID"""
    for task in tasks_db:
        if task.id == task_id:
            return task
    return None

def update_task(task_id: int, updated_task: Task) -> Optional[Task]:
    """Atualiza uma tarefa existente"""
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            updated_task.id = task_id
            updated_task.created_at = task.created_at
            tasks_db[index] = updated_task
            return updated_task
    return None

def delete_task(task_id: int) -> bool:
    """Remove uma tarefa do banco"""
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return True
    return False