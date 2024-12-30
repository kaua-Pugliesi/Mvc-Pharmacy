from typing import Dict
class PeopleLoginController:
    def login(self, login_finder_informations: Dict) -> Dict:
        try:
            self.__validate_fields(login_finder_informations)
            #enviar para models
            response = self.__format_response(login_finder_informations)
            return{"success": True, "message" : response}
        except Exception as error:
            return{"success": False, "message" : str(error)}
        
    def __validate_fields(self, login_finder_informations: Dict) -> None:
        if not isinstance(login_finder_informations["user"], str): # será substituido por validação específica
            raise Exception('Campo user Incorreto !')
        
        if not isinstance(login_finder_informations["password"], str): # será substituido por validação específica
            raise Exception('campo senha incorreta!')
    
    def __format_response(self, login_finder_informations: Dict) -> Dict: 
        return{
            "count": 1,
            "type": "employee",
            "attributes": login_finder_informations
        }
        
