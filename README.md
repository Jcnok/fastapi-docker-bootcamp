# To-Do List API (FastAPI)
Uma API simples para gerenciar tarefas (CRUD) construída com FastAPI.

![FastAPI](https://img.shields.io/badge/FastAPI-0.104-blue)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

##  Requisitos
- Python 3.10+
- pip
- (Opcional) Docker e Docker Compose

---

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Executando o Projeto
```bash
uvicorn app.main:app --reload
```

**Acesse:**
- Swagger UI → http://localhost:8000/docs
- ReDoc → http://localhost:8000/redoc

  
---

## Endpoints

### Criar tarefa

- **POST** `/todos/`

**Body exemplo:**
```json
{
  "title": "Estudar FastAPI",
  "description": "Completar bootcamp",
  "completed": false
}
```

**Exemplo curl:**
```bash
curl -X POST "http://localhost:8000/todos/" \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar FastAPI", "description": "Completar bootcamp", "completed": false}'
```

### Listar tarefas

- **GET** `/todos/?skip=0&limit=100`
- **Suporta query params:** `skip` (>=0), `limit` (1-1000)
```bash
curl "http://localhost:8000/todos/?skip=0&limit=100"
```

### Buscar tarefa por ID

- **GET** `/todos/{id}`
```bash
curl "http://localhost:8000/todos/1"
```
  
### Atualizar tarefa
- **PUT** `/todos/{id}`

**Body parcial ou total:**
```json
{
  "title": "Novo título",
  "completed": true
}
```
```bash
curl -X PUT "http://localhost:8000/todos/1" \
 -H "Content-Type: application/json" \
 -d '{"completed": true}'
```

### Deletar tarefa

**DELETE** `/todos/{id}`
```bash
curl -X DELETE "http://localhost:8000/todos/1"
```

## Testes
```bash
pytest -v
```

## Estrutura do Projeto
```txt
app/
 ├── main.py
 ├── models/
 │   └── todo.py
 └── routes/
     └── todos.py
```

---

## Boas Práticas e Dicas
- Use a documentação automática do FastAPI em `/docs` para testar rapidamente.
- Mensagens de erro estão em PT-BR e usam os status HTTP corretos (201, 404, 422, 204).
- Para persistência real, troque o banco em memória por um banco SQL (SQLite/PostgreSQL).

## Roadmap
- Persistência com banco de dados
- Autenticação e autorização (JWT)
- Paginação e filtros avançados

## Contribuição
**1.** Faça um fork do repositório

**2.** Crie uma branch:
```bash
git checkout -b feat/minha-feature
```
**3.** Commit:
```bash
git commit -m "feat: minha feature"
```
**4.** Push:
```bash
git push origin feat/minha-feature
```
**5.** Abra um Pull Request.

## Participantes
- Faça fork e branch
- Crie issues para sugestões e bugs
- Combine atividades via issues ou discussões

Adicione seu nome na lista conforme contribuir!

https://github.com/Jcnok

https://github.com/goncasthiago

https://github.com/Fernando599

https://github.com/Michelleyxz
