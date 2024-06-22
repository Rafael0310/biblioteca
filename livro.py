from dataclasses import dataclass

lista_livros = []

@dataclass
class Livro:
    titulo: str
    autor: str
    disponivel: bool
        
    def adicionar_livro():
        titulo = input('Informe o título do livro:\n').strip()
        autor = input('Informe o nome do autor do livro:\n')
        lista_livros.append(Livro(titulo=titulo, autor=autor, disponivel=True))
        print(f'Livro adicionado com sucesso!\nTítulo: {titulo}\nAutor: {autor}')