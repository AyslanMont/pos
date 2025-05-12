from fastapi import FastAPI, HTTPException
from models import Emprestimo, Usuario, Livro, Biblioteca

app = FastAPI()

usuarios = dict()
livros = dict()
bibliotecas = dict()
emprestimos = dict()
usuario_id = 1
livro_id = 1
biblioteca_id = 1
emprestimo_id = 1


@app.post("/usuarios/", response_model=Usuario)
def criar_usuarios(usuario: Usuario):
    global usuario_id
    usuarios[usuario_id] = usuario
    usuario_id += 1
    return usuario


@app.delete("/usuarios/", response_model=Usuario)
def apaga_usuarios(id: int):
    if id in usuarios:
        usuario_deletado = usuarios.pop(id)
        return usuario_deletado
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")


@app.get("/usuarios/", response_model=dict[int, Usuario])
def lista_usuarios():
    return usuarios


@app.post("/livros/", response_model=Livro, status_code=201)
def criar_livros(livro: Livro):
    global livro_id
    livros[livro_id] = livro
    livro_id += 1
    return livro


@app.delete("/livros/", response_model=Livro)
def apaga_livros(id: int):
    if id in livros:
        livro_deletado = livros.pop(id)
        return livro_deletado
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")


@app.get("/livros/", response_model=dict[int, Livro])
def lista_livros():
    return livros


@app.post("/biblioteca/", response_model=Biblioteca, status_code=201)
def criar_biblioteca(biblioteca: Biblioteca):
    global biblioteca_id
    bibliotecas[biblioteca_id] = biblioteca
    biblioteca_id += 1
    return biblioteca


@app.delete("/biblioteca/", response_model=Biblioteca)
def apaga_biblioteca(id: int):
    if id in bibliotecas:
        biblioteca_deletada = bibliotecas.pop(id)
        return biblioteca_deletada
    else:
        raise HTTPException(status_code=404, detail="Biblioteca não encontrada!")


@app.get("/biblioteca/", response_model=dict[int, Biblioteca])
def lista_biblioteca():
    return bibliotecas


@app.post("/emprestimo/", response_model=Emprestimo, status_code=201)
def criar_emprestimo(emprestimo: Emprestimo):
    global emprestimo_id
    emprestimos[emprestimo_id] = emprestimo
    emprestimo_id += 1
    return emprestimo


@app.delete("/emprestimo/", response_model=Emprestimo)
def apaga_emprestimo(id: int):
    if id in emprestimos:
        emprestimo_deletado = emprestimos.pop(id)
        return emprestimo_deletado
    else:
        raise HTTPException(status_code=404, detail="Usuário não encontrado!")


@app.get("/emprestimo/", response_model=dict[int, Emprestimo])
def lista_emprestimo():
    return emprestimos
