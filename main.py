# Import bibliotecas
import os

# Import cursor + methods
from connection import cursor

os.system('cls' if os.name=='nt' else 'clear')
while True:
    opt = int(input('O que deseja fazer?\n\n1 - Adicionar usuário\n2 - Adicionar livro\n3 - Realizar Empréstimo\n4 - Realizar devolução\n5 - Consultar livros\n0 - Sair\n'))

    match opt:
        case 1:
            pass

        case 2:
            pass

        case 3:
            pass

        case 4:
            pass
        
        case 5:
            pass    

        case 0:
            print('Encerrando...')
            exit()

        case _:
            os.system('cls' if os.name =='nt' else 'clear')
            print('Opção inválida! Tente novamente.')