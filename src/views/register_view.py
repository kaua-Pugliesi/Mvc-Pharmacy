import os
from typing import Dict

class RegisterView:
    def registry_view (self) -> Dict:
        os.system('cls||clear')
        
        print('Cadastra Usuário \n\n')
        login = input('Insira seu usuário: ')
        Password = input('Insira sua senha: ')
        name = input('Insira seu nome completo: ')
        
        registry_informations = {
            "user": login,
            "password" : Password,
            "name" : name
        }
        
        return registry_informations
    
    def registry_user_success(self, message: Dict) -> None:
        os.system('cls||clear')
        success_message = ''' 
            Usuário cadastrado com sucesso, contate o Ti para liberar seu acesso !
        '''
        print(success_message)
        
    def registry_user_fail(self, error: str) -> None:
        os.system('cls||clear')
        fail_message = f'''
            Falha ao cadastrar usuário
            Erro: { error }
        '''
        print(fail_message)