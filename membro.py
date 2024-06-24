# Importando bibliotecas
import os
from dataclasses import dataclass

# Importando métodos e classes
from metodos import continuar

from livro import (
    Livro,
    lista_livros,
    livros_disponiveis
)

lista_membros = []
livros_emprestados = []

@dataclass
class Membro:
    id_membro: int
    nome: str

    @staticmethod
    # Função para adicionar membro
    def adicionar_membro():
        os.system('cls' if os.name == 'nt' else 'clear')

        while True:
            try:
                id_membro = input('Informe o ID do membro:\n')
                # Verifica se o membro já está na listra, caso positivo, informa ao usuário, caso negativo, solicita os dados do novo membro
                if any(membro.id_membro == id_membro for membro in lista_membros):
                    print('''
    __________________________________________\n
        Esse membro já foi registrado!''')
        
                # Registro dos dados do usuário
                else:
                    nome = input('Informe o nome do membro:\n')
                    lista_membros.append(Membro(id_membro=id_membro, nome=nome))
                    print(f'Membro adicionado com sucesso!\nID: {id_membro}\nNome: {nome}')

            except ValueError:
                print('Por favor, insira um número inteiro')
            except:
                print('Erro inesperado.')

            finally:
                if not continuar('registrando membros'):
                    break

    @staticmethod
    # Função para emprestar livro
    def emprestar_livro():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            try:    
                id_membro = int(input('Informe o ID do membro qual está emprestando o livro:\n'))
                # Verifica se o ID digitado existe na lista do objeto Membro 
                if any(membro.id_membro == id_membro for membro in lista_membros):
                    isbn_livro = int(input('Qual o ISBN do livro que será emprestado?\n'))
                    # Verifica se o ISBN digitado exista na lista do objeto Livro
                    if any(livro.isbn == isbn_livro for livro in lista_livros):
                        # Verifica se o livro está disponível ou não
                        if any(livro == isbn_livro for livro in livros_disponiveis):
                            livros_disponiveis.remove(isbn_livro)
                            print('Livro disponível para empréstimo! Solicite devolução em até 5 dias úteis.')
                        else:
                            livros_emprestados.append(isbn_livro)
                            print('Livro não está disponível para empréstimo! Solicite que retorne outro dia.')
                            
                    else:
                        print('O ISBN do livro não foi localizado no sistema.')
                else:
                    print('O ID do membro não foi localizado no sistema.')
                    
            except ValueError:
                print('Por favor, insira um número inteiro.')
            except:
                print('Erro inesperado.')

            finally:
                if not continuar('emprestando livros'):
                    break
        

    # Função para devolver livro
    def devolver_livro():
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            try:
                id_membro = int(input('Informe o ID do membro qual está emprestando o livro:\n'))
                # Verifica se o ID digitado existe na lista do objeto Membro 
                if any(membro.id_membro == id_membro for membro in lista_membros):
                    isbn_livro = int(input('Qual o ISBN do livro que será devolvido?\n'))
                    # Verifica se o ISBN digitado exista na lista do objeto Livro
                    if any(livro.isbn == isbn_livro for livro in lista_livros):
                        # Verifica se o livro foi emprestado ou não
                        if any(livro == isbn_livro for livro in livros_emprestados):
                            print('O livro foi devolvido e agora está disponível para empréstimo.')
                        else:
                            print('Este livro não foi empréstado até o momento.')

                    else:
                        print('O ISBN do livro não foi localizado no sistema.')
                else:
                    print('O ID do membro não foi localizado no sistema.')

            except ValueError:
                print('Por favor, insira um número inteiro.')
            except:
                print('Erro inesperado.')

            finally:
                if not continuar('emprestando livros'):
                    break