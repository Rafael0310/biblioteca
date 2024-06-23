# Importando bibliotecas
import os
from dataclasses import dataclass

# Importando métodos e classes
from metodos import (
    continuar_registro
)

from livro import (
    Livro,
    lista_livros
)

lista_membros = []
livro_encontrado = False

@dataclass
class Membro:
    id_membro: int
    nome: str

    # Função para adicionar um novo membro
    def adicionar_membro():
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            id_membro = input('Informe o ID do membro:\n')
            nome = input('Informe o nome do membro:\n')
            lista_membros.append(Membro(id_membro=id_membro, nome=nome))
            print(f'Membro adicionado com sucesso!\nID: {id_membro}\nNome: {nome}')

            if continuar_registro('registrar','membro'):
                continue
            else:
                break

    # Função para emprestar livro
    def emprestar_livro():
        clivro = 'teste'
        for livro in lista_livros:
            if clivro == livro.titulo:
                print('ok')
            else:
                print('não ok')

    # Função para devolver livro
    def devolver_livro():
        clivro = 'teste'
        for livro in lista_livros:
            if clivro == livro.titulo:
                print('ok')
            else:
                print('não ok')