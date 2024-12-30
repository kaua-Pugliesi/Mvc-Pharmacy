from src.views.register_view import RegisterView
from src.controllers.register_controller import PropleRegisterController

def register_constructor():
    registry_view = RegisterView() #objetos geralmente são snake e classe em camell #instancia de view
    Prople_Register_Controller = PropleRegisterController() #instacia de controller
    
    registry_informations = registry_view.registry_view()#pega informações
    response = Prople_Register_Controller.register(registry_informations)#enviar informações para controller
    
    if response["success"]:
        registry_view.registry_user_success(response["message"])
    else:
        registry_view.registry_user_fail(response["error"])