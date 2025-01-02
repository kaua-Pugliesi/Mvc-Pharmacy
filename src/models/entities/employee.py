class Employee:
    def __init__(self, id: str, name: str, username: str, cpf: str, adress : str, phone: str, password: str, hiredate: str) -> None: #metodo construtor apenas para definir a classe
        self.id = id
        self.name = name
        self.username = username
        self.cpf = cpf
        self.adress = adress
        self.phone = phone
        self.password = password
        self.hiredate = hiredate