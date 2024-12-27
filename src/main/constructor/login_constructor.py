from src.views.login_view import LoginView

def login_constructor():
    login_view = LoginView()
    #controller
    
    login_finder_informations = login_view.do_login_view()
    #enviar para controller