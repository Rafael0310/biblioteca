# Importando bibliotecas
import os
from dataclasses import dataclass

# Importando metodos
from metodos import continuar_registro

lista_livros = []

@dataclass
class Livro:
    titulo: str
    autor: str
    disponivel: bool
        
    def adicionar_livro():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            titulo = input('Informe o título do livro:\n').lower().strip()
            autor = input('Informe o nome do autor do livro:\n')
            lista_livros.append(Livro(titulo=titulo, autor=autor, disponivel=True))
            print(f'Livro adicionado com sucesso!\nTítulo: {titulo}\nAutor: {autor}')

            if continuar_registro('registrar','livro'):
                continue
            else:
                break

