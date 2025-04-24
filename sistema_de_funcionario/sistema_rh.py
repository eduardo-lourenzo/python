from funcionarios import Funcionario, FuncionarioComum, Gerente, logar_acao

class SistemaRH():
    def __init__(self):
        self.__lista_de_funcionarios = []
    
    def set_funcionario(self, funcionario: Funcionario):
        self.__lista_de_funcionarios.append(funcionario)
        
    @logar_acao
    def __mostrar_bonus(self, funcionario: Funcionario) -> float:
        return funcionario.calcular_bonus()

    def listar_bonuses(self):
        for funcionario in self.__lista_de_funcionarios:
            self.mostrar_bonus(funcionario)
    
if __name__ == "__main__":
    rh = SistemaRH()
    
    funcionarios_comuns = [
        FuncionarioComum("Alice",   3000.00),
        FuncionarioComum("Carlos",  3500.00),
        FuncionarioComum("Bruna",   4000.00),
        FuncionarioComum("Daniel",  4500.00),
        FuncionarioComum("Elisa",   5000.00),
        FuncionarioComum("Fernando",5500.00),
        FuncionarioComum("Gabriela",6000.00),
        FuncionarioComum("Henrique",6500.00),
        FuncionarioComum("Irene",   7000.00)
    ]

    gerentes = [
        Gerente("João", 10000.00,   250.00),
        Gerente("Karla",12500.00,   500.00),
        Gerente("Lucas",15000.00,   750.00)
    ]
    
    for index in range(9):
       
        if index % 3 == 0:
            rh.set_funcionario(gerentes[index // 3])
            rh.set_funcionario(funcionarios_comuns[index])
        else:
            rh.set_funcionario(funcionarios_comuns[index])
            
    rh.listar_bonuses()
    