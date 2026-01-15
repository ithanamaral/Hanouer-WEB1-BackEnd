from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db, engine
import models
import uvicorn

# Cria as tabelas no banco caso elas não existam
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# --- SCHEMAS (Regras de Entrada de Dados) ---

class LoginSchema(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    name: str
    email: str
    cpf: str
    password: str

class UserUpdate(BaseModel):
    name: str
    email: str
    password: str

# --- ROTAS DE AUTENTICAÇÃO ---

@app.post("/login")
def login(user: LoginSchema, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == user.email).first()
    
    if not usuario:
        raise HTTPException(status_code=401, detail="E-mail ou senha incorretos")

    if usuario.password == user.password:
        return {
            "status": "success", 
            "message": "Login realizado!", 
            "user_email": usuario.email,
            "user_cpf": usuario.cpf 
        }
    
    raise HTTPException(status_code=401, detail="E-mail ou senha incorretos")

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(models.Usuario).filter(models.Usuario.email == user.email).first():
        raise HTTPException(status_code=400, detail="Este e-mail já está cadastrado.")
    
    if db.query(models.Usuario).filter(models.Usuario.cpf == user.cpf).first():
        raise HTTPException(status_code=400, detail="Este CPF já está cadastrado.")

    novo_usuario = models.Usuario(
        name=user.name,
        email=user.email,
        cpf=user.cpf,
        password=user.password 
    )

    try:
        db.add(novo_usuario)
        db.commit()
        db.refresh(novo_usuario)
        return {"status": "success", "message": "Usuário criado com sucesso!"}
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Erro ao salvar no banco de dados.")



# --- ROTAS DE PERFIL (CRUD) ---
@app.get("/perfil/{user_cpf}")
def get_perfil(user_cpf: str, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.cpf == user_cpf).first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return {
        "name": usuario.name,
        "email": usuario.email,
        "password": usuario.password,
        "cpf": usuario.cpf
    }

@app.put("/perfil/update/{user_cpf}")
def update_perfil(user_cpf: str, data: UserUpdate, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.cpf == user_cpf).first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    usuario.name = data.name
    usuario.email = data.email
    usuario.password = data.password
    
    db.commit()
    return {"status": "success", "message": "Perfil atualizado com sucesso!"}



# --- ROTAS DE PRODUTOS ---
@app.get("/produtos")
def listar_produtos():
    return [
        {"id": 1, "nome": "Biscoitinho Hanouer", "preco": 150.00},
        {"id": 2, "nome": "Tigela Premium", "preco": 25.00}
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)