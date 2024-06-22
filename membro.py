from dataclasses import dataclass

lista_membros = []

@dataclass
class Membro:
    id_membro: int
    nome: str
    livros_emprestados = []

def adicionar_membro():
    id_membro = input('Informe o ID do membro:\n')
    nome = input('Informe o nome do membro:\n')
    lista_membros.append(Membro(id_membro=id_membro, nome=nome))
    print(f'Membro adicionado com sucesso!\nID: {id_membro}\nNome: {nome}')


adicionar_membro()