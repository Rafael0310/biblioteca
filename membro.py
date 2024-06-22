from dataclasses import dataclass
from livro import (
    Livro,
    lista_livros
)

lista_membros = {}
livro_encontrado = False

@dataclass
class Membro:
    id_membro: int
    nome: str

    ids_membros = set()

    # Função para adicionar um novo membro
    def adicionar_membro():
        id_membro = input('Informe o ID do membro:\n')
        nome = input('Informe o nome do membro:\n')
        lista_membros.append(Membro(id_membro=id_membro, nome=nome))
        print(f'Membro adicionado com sucesso!\nID: {id_membro}\nNome: {nome}')

    # Função para emprestar livro
    def emprestar_livro():
        livro_interessado = input('Qual livro será emprestado? ').strip
        for livro in lista_livros.values():
            if livro == livro_interessado:
                livro_encontrado = True
                break
        
        #if livro_encontrado:
        #    lista_membros.append(livro_interessado)
        #    print(f'O livro: {livro_interessado} foi emprestado\n')
        #else:
        #    print('O livro não foi localizado')