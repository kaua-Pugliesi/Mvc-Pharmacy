from .constructor.autentication_process import autentication_process
from .constructor.login_constructor import login_constructor
from .constructor.register_constructor import register_constructor
def start() -> None:
    while True:
        command = autentication_process()

        if command == '1': 
            login_constructor()
        elif command == '2':
            register_constructor()
        elif command == '3':
            exit()
        else:
            print('\n comando não encontrado!! \n\n')
