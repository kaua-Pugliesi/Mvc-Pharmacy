from .constructor.autentication_process import autentication_process

def start() -> None:
    while True:
        command = autentication_process()

        if command == '1': 
            print('comando 1 foi acionado')
        elif command == '2':
            print('comando 2 foi acionado')
        elif command == '3':
            exit()
        else:
            print('\n comando não encontrado!! \n\n')
