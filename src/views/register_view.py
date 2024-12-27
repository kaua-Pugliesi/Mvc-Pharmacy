import os
from typing import Dict

class RegisterView:
    def registry_view (self) -> Dict:
        os.system('cls||clear')
        
        print('Cadastra Usuário \n\n')
        login = input('Insira seu usuario: ')
        Password = input('Insira sua senha: ')
        name = input('Insira seu nome completo: ')
        
        registry_informations = {
            "user": login,
            "password" : Password,
            "name" : name
        }
        
        return registry_informations