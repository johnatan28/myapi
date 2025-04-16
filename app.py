from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

 # Banco de dados fictício (lista na memória)
empresa_db = []


# # Modelo de usuário (validação automática)
class Usuario(BaseModel):
     id: int
     nome: str
     email: str
     cpf: str

 # Rota para listar todos os usuários
@app.get("/usuarios")

def listar_usuarios():
     return empresa_db

# # Rota para adicionar um novo usuário
@app.post("/usuarios")

def criar_usuario(usuario: Usuario):
     # Verifica se já existe um usuário com o mesmo ID
     for u in empresa_db:
         if u["id"] == usuario.id:
             raise HTTPException(status_code=400, detail="ID já existe.")
     empresa_db.append(usuario.dict())
     return {"mensagem": "Usuário criado com sucesso."}

 # Rota para buscar usuário por ID
@app.get("/usuarios/{usuario_id}")

def buscar_usuario(usuario_id: int):
     for usuario in empresa_db:
         if usuario["id"] == usuario_id:
             return usuario
     raise HTTPException(status_code=404, detail="Usuário não encontrado.")

# # Rota raiz
# @app.get("/")
# def read_root():
#     return {"mensagem": "Olá, mundo!"}


# # Rota com parâmetro
# @app.get("/saudacao/{nome}")
# def saudar(nome: str):
#      return{"mensagem": f"Olá, {nome}"}
