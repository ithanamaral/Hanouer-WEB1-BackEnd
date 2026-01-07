from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import models
import uvicorn

app = FastAPI()

# Configuração de CORS para o seu React (Porta 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo que o FastAPI espera receber do React
class LoginSchema(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(user: LoginSchema, db: Session = Depends(get_db)):
    # 1. Busca no SQLite
    usuario = db.query(models.Usuario).filter(models.Usuario.email == user.email).first()
    
    # Debug no terminal
    if not usuario:
        print(f"ERRO: Usuário {user.email} não encontrado.")
        raise HTTPException(status_code=401, detail="E-mail ou senha incorretos")

    # 2. Comparação (Garantindo que a coluna no banco é .password)
    if usuario.password == user.password:
        print(f"SUCESSO: {usuario.email} logado.")
        return {"status": "success", "message": "Login realizado!", "user": usuario.email}
    else:
        print(f"ERRO: Senha incorreta para {usuario.email}")
        raise HTTPException(status_code=401, detail="E-mail ou senha incorretos")

@app.get("/produtos")
def listar_produtos():
    return [
        {"id": 1, "nome": "Biscoitinho Hanouer", "preco": 150.00},
        {"id": 2, "nome": "Tigela Premium", "preco": 25.00}
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)