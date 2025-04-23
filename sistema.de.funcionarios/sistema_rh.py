from funcionarios import *

class SistemaRH():
    @logar_acao
    def mostrar_bonus(self, funcionario: Funcionario) -> float:
        return funcionario.calcular_bonus()
