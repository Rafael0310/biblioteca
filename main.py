# Import bibliotecas
import os
from datetime import datetime

# Import cursor + methods
from connection import conn
from db import (
    ADD_USER,
    ADD_BOOK,
    EMP_BOOK,
    DLV_BOOK
)

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def adicionar_usuario():
    try:
        nome = input('Digite o nome do usuário: ')
        email = input('Digite o email do usuário: ')
        data = datetime.now().date()

        with conn.cursor() as cursor:
            cursor.execute(ADD_USER, (nome, email, data,))
            conn.commit()

            print('Usuário adicionado com sucesso!\n')
            clear()

    except Exception as e:
        clear()
        print(f"Erro detectado: {e.__class__.__name__}\n{str(e)}\n")

def adicionar_livro():
    try:
        titulo = input('Digite o título do livro: ')
        autor = input('Digite o nome do autor: ')
        categoria = input('Digite a categoria do livro: ')

        with conn.cursor() as cursor:
            cursor.execute(ADD_BOOK, (titulo, autor, categoria, 1,))
            conn.commit()

            clear()
            print('\nLivro adicionado com sucesso!\n')

    except Exception as e:
        clear()
        print(f"Erro detectado: {e.__class__.__name__}\n{str(e)}\n")

def emprestar_livro():
    try:
        clear()

        id_usuario = int(input('Digite o ID do usuário que irá pegar o livro: '))

        with conn.cursor() as cursor:
            cursor.execute('SELECT id FROM usuarios WHERE id=%s', (id_usuario,))
            check_usuario = cursor.fetchone()

        if check_usuario:
            try:
                id_livro = int(input('Digite o ID do livro que será emprestado: '))

                with conn.cursor() as cursor:
                    cursor.execute('SELECT id FROM livros WHERE id=%s', (id_livro,))
                    check_livro = cursor.fetchone()

                if check_livro:
                    data_emprestimo = datetime.now().date()

                    with conn.cursor() as cursor:
                        cursor.execute(EMP_BOOK, (id_usuario, id_livro, data_emprestimo,))

                        print('Livro emprestado com sucesso!\n')
                
                else:
                    clear()
                    print('ID de livro não localizado!\n')

            except TypeError:
                clear()
                print('Por favor, insira um número inteiro.\n')

            except Exception as e:
                print(f"Erro detectado: {e.__class__.__name__}\n{str(e)}\n")


        else:
            print('ID de usuário não localizado!')

    except TypeError:
        print('Por favor, insira um número inteiro.')

    except Exception as e:
        print(f"Erro detectado: {e.__class__.__name__}\n{str(e)}\n")

clear()

while True:
    opt = input('O que deseja fazer?\n\n1 - Adicionar usuário\n2 - Adicionar livro\n3 - Realizar empréstimo\n4 - Realizar devolução\n5 - Consultar\n0 - Sair\n')

    match opt:
        case '1':
            adicionar_usuario()

        case '2':
            adicionar_livro()

        case '3':
            emprestar_livro()

        case '4':
            pass
        
        case '5':
            clear()
            while True:
                opt = input('O que deseja consultar?\n\n1 - Listar todos os livros disponíveis\n2 - Listar os livros emprestados a determinado usuário\n3 - Listar todos os usuários e o número de empréstimos realizados\n0 - Sair\n')  
                
                match opt:
                    case '1':
                        clear()

                        with conn.cursor() as cursor:
                            cursor.execute('SELECT id, titulo, autor, categoria FROM livros WHERE disp=1')
                            books = cursor.fetchall()
                            cursor.close()

                        if books:
                            for book in books:
                                print(f'ID: {book[0]}, Título: {book[1]}, Autor: {book[2]}, Categoria: {book[3]}')

                            opt = input('\nO que deseja fazer?\n1 - Realizar empréstimo\n0 - Voltar ao menu\n')
                            match opt:
                                case '1':
                                    emprestar_livro()
                                
                                case '0':
                                    clear()
                                    break

                                case _:
                                    clear()
                                    print('Opção inválida.\n')
                            break
                        
                        else:
                            print('Não existem livros disponíveis')
                    
                    case '2':
                        pass

                    case '3':
                        pass

                    case '0':
                        clear()
                        break

                    case _:
                        clear()
                        print('Opção inválida! Tente novamente.\n')

        case '0':
            clear()
            print('Encerrando...')
            exit()

        case _:
            clear()
            print('Opção inválida! Tente novamente.')