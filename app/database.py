from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração Padrão do SQLite
DATABASE_URL = "sqlite:///./teste.db" 
engine = create_engine(
    DATABASE_URL, 
    # Necessário para SQLite com FastAPI
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    Dependência do FastAPI para fornecer uma sessão de banco de dados
    e garantir que ela seja fechada após o uso.
    """
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()