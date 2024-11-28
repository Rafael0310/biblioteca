# Import bibliotecas
import os
from datetime import datetime

# Import cursor + methods
from connection import cursor, conn
from db import (
    ADD_USER,
    ADD_BOOK
)

os.system('cls' if os.name=='nt' else 'clear')
while True:
    opt = int(input('O que deseja fazer?\n\n1 - Adicionar usuário\n2 - Adicionar livro\n3 - Realizar Empréstimo\n4 - Realizar devolução\n5 - Consultar\n0 - Sair\n'))

    match opt:
        case 1:
            try:
                nome = input('Digite o nome do usuário: ')
                email = input('Digite o email do usuário: ')
                data = datetime.now().date()

                cursor.execute(ADD_USER, (nome, email, data,))
                conn.commit()

                os.system('cls' if os.name=='nt' else 'clear')
                print('Usuário adicionado com sucesso!\n')
            except Exception as e:
                print(f'Ops, algo deu errado!{e}')

        case 2:
            try:
                titulo = input('Digite o título do livro: ')
                autor = input('Digite o nome do autor: ')
                categoria = input('Digite a categoria do livro: ')

                cursor.execute(ADD_BOOK, (titulo, autor, categoria, 1,))
                conn.commit()

                os.system('cls' if os.name=='nt' else 'clear')
                print('Livro adicionado com sucesso!\n')
            except Exception as e:
                print(f'Ops, algo deu errado!\n{e}')

        case 3:
            pass

        case 4:
            pass
        
        case 5:
            os.system('cls' if os.name=='nt' else 'clear')
            while True:
                opt = int(input('O que deseja consultar?\n\n1 - Listar todos os livros disponíveis\n2 - Listar os livros emprestados por um determinado usuário\n3 - Listar todos os usuários e o número de empréstimos realizados\n0 - Sair\n'))    
                
                match opt:
                    case 1:
                        cursor.execute('SELECT * FROM livros WHERE disp=1')
                
                    case 2:
                        pass

                    case 3:
                        pass

                    case 0:
                        os.system('cls' if os.name=='nt' else 'clear')
                        break

                    case _:
                        os.system('cls' if os.name=='nt' else 'clear')
                        print('Opção inválida! Tente novamente.\n')

        case 0:
            os.system('cls' if os.name=='nt' else 'clear')
            print('Encerrando...')
            exit()

        case _:
            os.system('cls' if os.name =='nt' else 'clear')
            print('Opção inválida! Tente novamente.')