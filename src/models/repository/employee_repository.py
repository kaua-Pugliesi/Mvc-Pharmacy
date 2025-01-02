from src.models.entities.employee import Employee

class EmployeeRepository:
    def __init__(self) -> None:
        self.__employee = []
        
    def registry_employee(self, employee: Employee) -> None:
        self.__employee.append(employee)
    
    
    
    