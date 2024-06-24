import os
from dataclasses import dataclass

# Importando metodos
from metodos import continuar

lista_livros = []
livros_disponiveis = []

@dataclass
class Livro:
    isbn: int
    titulo: str
    autor: str

    @staticmethod
    # Função para adicionar livro
    def adicionar_livro():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo = input('Informe o título do livro:\n').lower().strip()
            # Verificar se o livro já está na lista, caso positivo, informa ao usuário, caso negativo, solicita as informações do livro
            if any(livro.titulo == titulo for livro in lista_livros):
                print('''
__________________________________________\n
      Esse livro já foi registrado!''')
                
            # Registro das informações do livro
            else:
                isbn = len(lista_livros) + 1
                autor = input('Informe o nome do autor do livro:\n')
                livros_disponiveis.append(isbn)
                lista_livros.append(Livro(isbn=isbn, titulo=titulo, autor=autor))
                print(f'''
__________________________________________\n
      Livro adicionado com sucesso!
__________________________________________\n
             ISBN: {isbn}
             Título: {titulo}
             Autor: {autor}''')

            if not continuar('registrando livros'):
                break