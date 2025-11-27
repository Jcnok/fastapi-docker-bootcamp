from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Importa a Base para criação das tabelas e a função de dependência (get_db)
from .database import Base, engine, get_db
# Importa os modelos User e Task que você definiu
from .models import User, Task 

# Importações de Segurança (passlib)
from passlib.context import CryptContext

# --- 1. CONFIGURAÇÃO E CRIAÇÃO DE TABELAS ---

# Cria todas as tabelas (users e tasks) no banco de dados (SQLite)
Base.metadata.create_all(bind=engine) 

app = FastAPI(
    title="FastAPI To do List Bootcamp API",
    description="API Refatorada com correção de bugs e autenticação básica.",
    version="1.0.0"
)

# --- 2. UTILS DE SEGURANÇA (Inline) ---
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """Cria o hash da senha usando bcrypt."""
    return pwd_context.hash(password)

# --- 3. SCHEMAS PYDANTIC (Inline) ---

# Schemas de Usuário
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    class Config:
        from_attributes = True

# Schema para atualização parcial de tarefa (PATCH)
class TaskUpdatePartial(BaseModel):
    """Schema para a correção do bug: todos os campos são opcionais."""
    title: Optional[str] = Field(None, description="Novo título da tarefa.")
    description: Optional[str] = Field(None, description="Nova descrição da tarefa.")
    completed: Optional[bool] = Field(None, description="Novo status (True/False).")
    class Config:
        extra = "forbid" 

# --- 4. ROTAS DE USUÁRIO (Criação/Registro) ---

@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED, tags=["users"])
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """Registra um novo usuário e armazena a senha criptografada."""
    
    # 1. Verifica se o email já existe
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    # 2. Criptografa a senha antes de salvar
    hashed_password = get_password_hash(user.password)
    
    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password # Salva o hash
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

# --- 5. ROTAS DE TAREFAS (PATCH - Correção de Bug) ---

@app.patch("/tasks/{task_id}", tags=["tasks"])
def update_task_partial_endpoint(
    task_id: int, 
    task_data: TaskUpdatePartial, 
    db: Session = Depends(get_db) # Usa a dependência de sessão
):
    """
    Atualiza parcialmente uma tarefa (PATCH). 
    Corrige o bug de sobrescrever o 'status' se não for enviado,
    graças ao uso de exclude_unset=True.
    """
    
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    # A CHAVE DA CORREÇÃO: Pydantic ignora campos com valor None (não definidos)
    update_data = task_data.model_dump(exclude_unset=True) 
    
    # Aplica as mudanças
    for key, value in update_data.items():
        setattr(task, key, value) 

    db.commit()
    db.refresh(task)

    return {"message": "Tarefa atualizada com sucesso"}