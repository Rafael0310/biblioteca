def continuar(metodo):
    while True:
        try:

            continuar = int(input(f'''
__________________________________________\n
    Deseja continuar {metodo}?
__________________________________________\n
                1 - Sim
                2 - Não
__________________________________________\n
                  '''))
        
            match continuar:
                case 1:
                    continuar = True
                case 2:
                    continuar = False
                case _:
                    print('Opção inválida! Tente novamente.')
            
        except:
            print('As opções são: 1 - para continuar ou 2 - para voltar ao menu principal')
        finally:
            return continuar