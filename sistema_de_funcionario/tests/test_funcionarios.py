import pytest
from funcionarios import FuncionarioComum, Gerente

def test_funcionario_comum_calcula_bonus():
    funcionario = FuncionarioComum("João", 3000.00)
    assert funcionario.calcular_bonus() == 300.00

def test_gerente_calcula_bonus():
    gerente = Gerente("Maria", 5000.00, 500.00)
    assert gerente.calcular_bonus() == 1500.00

def test_set_salario_nao_aceita_negativo():
    funcionario = FuncionarioComum("João", 3000.00)
    funcionario.set_salario(-500.00)
    assert funcionario.get_salario() == 3000.00
