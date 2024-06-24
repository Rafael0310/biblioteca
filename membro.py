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
                id_membro = int(input('Informe o ID do membro:\n'))
                # Verifica se o membro já está na listra, caso positivo, informa ao usuário, caso negativo, solicita os dados do novo membro
                if any(membro.id_membro == id_membro for membro in lista_membros):
                    print('''
__________________________________________\n
     Esse membro já foi registrado!''')
        
                # Registro dos dados do usuário
                else:
                    nome = input('\nInforme o nome do membro:\n')
                    lista_membros.append(Membro(id_membro=id_membro, nome=nome))
                    print(f'''
__________________________________________\n
      Membro adicionado com sucesso!
__________________________________________
        ID: {id_membro}
        Nome: {nome}''')

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
        
        os.system('cls' if os.name == 'nt' else 'clear')
        # Verifica se existe pelo menos um livro e um membro registrado
        if lista_livros and lista_membros:
        
            while True:
                try:    
                    id_membro = int(input('Informe o ID do membro qual está emprestando o livro:\n'))
                    # Verifica se o ID digitado existe na lista do objeto Membro 
                    if any(membro.id_membro == id_membro for membro in lista_membros):
                        isbn_livro = int(input('\nQual o ISBN do livro que será emprestado?\n'))
                        # Verifica se o ISBN digitado exista na lista do objeto Livro
                        if any(livro.isbn == isbn_livro for livro in lista_livros):
                            # Verifica se o livro está disponível ou não
                            if any(livro == isbn_livro for livro in livros_disponiveis):
                                livros_emprestados.append(isbn_livro)
                                livros_disponiveis.remove(isbn_livro)
                                print('\nO livro foi devolvido com sucesso.')
                            else:
                                print('\nLivro não está disponível para empréstimo! Solicite que retorne outro dia.')
                                    
                        else:
                            print('\nO ISBN do livro não foi localizado no sistema.')
                    else:
                        print('\nO ID do membro não foi localizado no sistema.')
                            
                except ValueError:
                    print('\nPor favor, insira um número inteiro.')
                except:
                    print('\nErro inesperado.')

                finally:
                    if not continuar('emprestando livros'):
                        break
                    
        else:
            print('Registre pelo menos um membro e um livro para executar essa função')

    # Função para devolver livro
    def devolver_livro():
        os.system('cls' if os.name == 'nt' else 'clear')
        if lista_livros and lista_membros:
            while True:

                # Verifica se existe pelo menos um livro e um membro registrado
                    
                try:
                    id_membro = int(input('Informe o ID do membro qual está recebendo o livro:\n'))
                    # Verifica se o ID digitado existe na lista do objeto Membro 
                    if any(membro.id_membro == id_membro for membro in lista_membros):
                        isbn_livro = int(input('\nQual o ISBN do livro que será devolvido?\n'))
                        # Verifica se o ISBN digitado exista na lista do objeto Livro
                        if any(livro.isbn == isbn_livro for livro in lista_livros):
                            # Verifica se o livro foi emprestado ou não
                            if any(livro == isbn_livro for livro in livros_emprestados):
                                print('\nO livro foi devolvido com sucesso.')
                                livros_disponiveis.append(isbn_livro)
                                livros_emprestados.remove(isbn_livro)
                            else:
                                print('\nEste livro não foi empréstado até o momento.')

                        else:
                            print('\nO ISBN do livro não foi localizado no sistema.')
                    else:
                        print('\nO ID do membro não foi localizado no sistema.')

                except ValueError:
                    print('\nPor favor, insira um número inteiro.')
                except:
                    print('\nErro inesperado.')

                finally:
                    if not continuar('devolver outros'):
                        break

        else:
            print('Registre pelo menos um membro e um livro para executar essa função')

    def imprimir_livros_disponiveis():

        # Verifica existe algum livro registrado
        if lista_livros:    
            # Verifica se existem livros disponíveis
            if livros_disponiveis:
                for livro in lista_livros:
                    if any(livro_disponivel == livro.isbn for livro_disponivel in livros_disponiveis):
                        print(f'''
    __________________________________________\n
        ISBN: {livro.isbn}
        Título: {livro.titulo.capitalize()}
        Autor: {livro.autor}''')
            
            else:
                print('Não possuimos livros disponíveis no momento')
        else:
            print('Adicione pelo menos um livro antes de executar essa função.')
                
    def imprimir_livros_emprestados():
        
        if lista_livros:
            if livros_emprestados:
                for livro in lista_livros:
                    if any(livro_emprestado == livro.isbn for livro_emprestado in livros_emprestados):
                        print(f'''
    __________________________________________\n
        ISBN: {livro.isbn}
        Título: {livro.titulo.capitalize()}
        Autor: {livro.autor}''')
                
            else:
                print('Todos os livros estão disponíveis no momento')
        else:
            print('Adicione pelo menos um livro antes de executar essa função.')