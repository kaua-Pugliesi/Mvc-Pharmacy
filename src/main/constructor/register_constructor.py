from src.views.register_view import RegisterView

def register_constructor():
    registry_view = RegisterView() #objetos geralmente são snake e classe em camell
    #controller
    
    registry_informations = registry_view.registry_view()
    #enviar para controller