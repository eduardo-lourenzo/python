from funcionarios import Funcionario, FuncionarioComum, Gerente, logar_acao

class SistemaRH():
    @logar_acao
    def mostrar_bonus(self, funcionario: Funcionario) -> float:
        return funcionario.calcular_bonus()

if __name__ == "__main__":
    rh = SistemaRH()
    
    f = FuncionarioComum("João", 3000.00)
    g = Gerente("Maria", 5000.00, 500.00)
    
    rh.mostrar_bonus(f)
    rh.mostrar_bonus(g)