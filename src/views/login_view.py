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

    def do_login_success(self, message: Dict) -> None:
        os.system('cls||clear')
        success_message = ''' 
            Login efetuado com sucesso.
        '''
        print(success_message)
        
    def do_login_fail(self, error: str) -> None:
        os.system('cls||clear')
        fail_message = f''' 
            Erro no login.
            Erro: { error }
        '''
        print(fail_message)