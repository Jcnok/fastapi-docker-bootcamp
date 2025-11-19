# 📘 FastAPI + Docker Bootcamp

Projeto colaborativo para aplicar conceitos de API RESTful, FastAPI, Python, Docker e boas práticas de desenvolvimento.

## 🚀 Funcionalidades Implementadas

### ✔ Paginação no endpoint GET /tasks

Suporte a ```skip``` e ```limit```

Retorno com total, itens e metadados

Exemplo de resposta:

```json
{
  "total": 0,
  "skip": 0,
  "limit": 10,
  "items": []
} 
```

### ✔ CRUD de Tarefas (Tasks)

Criar tarefas

Listar tarefas (paginado)

Buscar tarefa por ID

Deletar tarefa

Validações completas com Pydantic v2

### 🧪 Testes Automatizados (Pytest)

Testes para GET, POST, DELETE

TestClient simulando requisições HTTP reais

Arquivo pytest.ini configurando o ambiente corretamente

Testes separados em tests/

### 🛡️ Validações (Pydantic v2)

Título: máximo de 100 caracteres

Descrição: máximo de 500 caracteres

Validador que remove espaços no início e fim

Erro se o título for vazio ou composto apenas de espaços

Uso correto de ConfigDict (Pydantic v2)

### 📂 Organização do Projeto

```
app/
 ├── main.py
 ├── models/
 │    └── models.py
 └── routers/
tests/
 └── system_test.py
pytest.ini
Dockerfile
README.md
```

## 🌐 API Desenvolvida

A API implementa um CRUD simples de tarefas (“Tasks”).

### 📌 Endpoints

### GET /

Retorna informações gerais (ex.: status inicial).

### GET /tasks

Lista tarefas com paginação.

Parâmetros Query:

```skip``` : inteiro — padrão 0

```limit``` : inteiro — padrão 10

Exemplo:
```
GET /tasks?skip=0&limit=10

GET /tasks/{task_id}
```
Busca uma tarefa pelo ID.

Exemplo:
```
GET /tasks/1
```

### POST /tasks


Cria uma nova tarefa.

Body : 

```json
{
  "title": "Aprender FastAPI",
  "description": "Estudar FastAPI e Docker",
  "completed": false
}
```

Validações:

-```title``` obrigatório

- Máximo 100 caracteres

- Não pode ser vazio ou só espaços

- ```description``` opcional, máximo 500 caracteres

- ```completed``` booleano

### DELETE /tasks/{task_id}

Remove uma tarefa existente.

Retorna:

- 204 No Content se excluída

- 404 se não existir

## ▶️ Como rodar o projeto localmente

🔧 1. Com Uvicorn (sem Docker)
Criar ambiente virtual
```
python -m venv venv
```
Ativar:

Windows:

```
venv\Scripts\activate
```

Linux/Mac:
```
source venv/bin/activate
```

2. Instalar dependências
```
pip install -r requirements.txt
```

Rodar o servidor localmente

```
uvicorn app.main:app --reload
```

Acesse:

http://127.0.0.1:8000

Documentação Swagger: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

## 🐳 Rodar com Docker

Build
```
docker build -t fastapi-bootcamp .
```
Run
```
docker run -d -p 8000:8000 fastapi-bootcamp
```

## 🤝 Contribuição

Faça fork e crie uma branch por feature

Abra issues para melhorias, bugs e dúvidas

Combine tarefas via issues/discussões

Atualize o README ao concluir funcionalidades

## 👥 Participantes

Adicione seu nome ao contribuir!

Julio Okuda - [https://github.com/Jcnok](https://github.com/Jcnok)

Thiago Debia - [https://github.com/goncasthiago](https://github.com/goncasthiago)