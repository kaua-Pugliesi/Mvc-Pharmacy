from typing import Dict
class PropleRegisterController:
    def register(self,registry_informations: Dict) -> Dict: # o self é usado para acessar os atributos e métodos da instância da classe.
        try:
            self.__validate_fields(registry_informations)
            #enviar para models para cadasto de dados
            response = self.__format_response(registry_informations)
            return {"success": True, "message" : response}
        except Exception as error:
            return{"success": False, "error": str(error) }
    
    
    def __validate_fields(self, registry_informations: Dict ) -> None:
        if not isinstance(registry_informations["user"], str):
            raise Exception('Campo user Incorreto !')
        
        if not isinstance(registry_informations["name"], str):
            raise Exception('Campo nome Incorreto !')
        
        if not isinstance(registry_informations["password"], str):
            raise Exception('campo senha incorreta!')
        
    def __format_response(self, registry_informations: Dict) -> Dict: 
        
        return{
            "count": 1,
            "type": "employee",
            "attributes": registry_informations
        }
        
        
            