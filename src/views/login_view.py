import os
from typing import Dict

class LoginView:
    def do_login_view(self) -> Dict:
        os.system('cls||clear')
        
        print('Fazer Login \n\n')
        login = input('Insira seu usuario: ')
        Password = input('Insira sua senha: ')
        
        login_finder_informations = {
            "user": login,
            "password" : Password
        }
        
        return login_finder_informations