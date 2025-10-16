from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à primeira API FastAPI no bootcamp!"}
