# Importação de bibliotecas
import os

# Importação de classes
from livro import Livro
from membro import Membro

while True:

    print('''
____________________________________\n
       Sistema bibliotecário
____________________________________\n
          Menu Principal
____________________________________\n
      1 - Adicionar membro
      2 - Adicionar livro
      3 - Emprestar livro
      4 - Devolver livro
      5 - Sair\n
____________________________________\n''')
    
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
                print('Encerrando...')
                quit()
            case _:
                os.system('cls')
                print('Opção inválida! Tente novamente.')
        
    except  ValueError:
        print('Por favor, insira um número inteiro.')