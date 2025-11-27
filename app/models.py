from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime # Importar para usar no campo de data/hora
from .database import Base # Importa sua Base declarativa

# --- MODELO USER (Atualizado com Senha e Relacionamento) ---

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String) # Campo para a senha HASHED

    # 1. Relacionamento com as Tarefas
    # Permite acessar user.tasks (lista de objetos Task)
    tasks = relationship("Task", back_populates="owner") 


# --- NOVO MODELO TASK (A TAREFA) ---

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    
    # Campos que você precisará para a lógica da API:
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow) # Armazena quando a tarefa foi criada
    
    # 2. Chave Estrangeira (Relacionamento com User)
    # owner_id liga esta tarefa ao ID de um usuário na tabela 'users'
    owner_id = Column(Integer, ForeignKey("users.id")) 
    
    # 3. Propriedade de Relacionamento
    # Permite acessar task.owner (objeto User)
    owner = relationship("User", back_populates="tasks")