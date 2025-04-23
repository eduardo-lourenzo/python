from abc import ABC, abstractmethod
        
class Funcionario (ABC):
        def __init__(self, nome: str, salario: float):
            self.__nome = nome
            self.__salario = salario
        
        @abstractmethod
        def calcular_bonus(self) -> float:
            pass
        
        def get_nome(self) -> str:
            return self.__nome
        
        def get_salario(self) -> float:
            return self.__salario
        
        def set_salario(self, salario: float):
            if salario > 0.0:
                self.__salario = salario
                
def logar_acao(func):
        def wrapper(*args, **kwargs):
            #mostrar_bonus(self, funcionario) => mostrar_bonus(args[0], args[1])  
            funcionario = args[1]
            
            bonus = func(*args, **kwargs)
            cargo = ""
            
            if isinstance(funcionario, FuncionarioComum):
                cargo = "funcionário"
            elif isinstance(funcionario, Gerente):
                cargo = "gerente"
            
            print(f"O bonus do {cargo} {funcionario.get_nome()} é de {bonus: .2f}")    
            
            return bonus
        return wrapper

class FuncionarioComum(Funcionario):
        def calcular_bonus(self) -> float:
            return self.get_salario() * 0.1


class Gerente(Funcionario):
        def __init__(self, nome: str, salario: float, bonus_adicional: float):
            super().__init__(nome, salario)
            self.__bonus_adicional = bonus_adicional
        
        def calcular_bonus(self):
            return self.get_salario() * 0.2 + self.__bonus_adicional
