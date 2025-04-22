from abc import ABC, abstractmethod

class Funcionario (ABC):
    def __init__(self, nome: str, salario: float):
        self.__nome = nome
        self.__salario = salario
    
    @abstractmethod
    def calcular_bonus() -> float:
        pass