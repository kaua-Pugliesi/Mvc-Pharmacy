from src.views.login_view import LoginView
from src.controllers.login_controller import PeopleLoginController

def login_constructor():
    login_view = LoginView()
    login_controller = PeopleLoginController()
    
    login_finder_informations = login_view.do_login_view()
    response = login_controller.login(login_finder_informations)
    
    if response["success"]:
        login_view.do_login_success(response["message"])
    else:
       login_view.do_login_fail(response["error"])