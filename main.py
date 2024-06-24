# Importação de bibliotecas
import os

# Importação de classes
from livro import Livro
from membro import Membro

while True:

    print('''
__________________________________________\n
          Sistema bibliotecário
__________________________________________\n
             Menu Principal
__________________________________________\n
      1 - Adicionar membro
      2 - Adicionar livro
      3 - Emprestar livro
      4 - Devolver livro
      5 - Imprimir livros disponívels
      6 - Imprimir livros emprestados
      7 - Sair\n
__________________________________________\n''')
    
    try:
        opcao = int(input('O que deseja? '))

        match opcao:
            case 1:
                Membro.adicionar_membro()

            case 2:
                Livro.adicionar_livro()

            case 3:
                Membro.emprestar_livro()

            case 4:
                
                Membro.devolver_livro()
            case 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                Membro.imprimir_livros_disponiveis()

            case 6:
                os.system('cls' if os.name == 'nt' else 'clear')
                Membro.imprimir_livros_emprestados()

            case 7:
                print('Encerrando...')
                quit()

            case _:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Opção inválida! Tente novamente.')
        
    except  ValueError:
        print('Por favor, insira um número inteiro.')