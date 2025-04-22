import unittest
from RelatorioDeMissao import RelatorioDeMissao
from RoboExplorador import RoboExplorador

class TestRelatorioDeMissao(unittest.TestCase):
    def test_heranca(self):
        relatorio = RelatorioDeMissao("Spirit", "Marte", 85, (("temperatura", -50), ("radiação", 2.5)))
        self.assertIsInstance(relatorio, RoboExplorador)

    def test_resumo(self):
        relatorio = RelatorioDeMissao("Spirit", "Marte", 85, (("temperatura", -50), ("radiação", 2.5)))
        self.assertEqual(relatorio.resumo(), ["temperatura: -50", "radiação: 2.5"])

    def test_contagem_leituras(self):
        relatorio = RelatorioDeMissao("Spirit", "Marte", 85, (("temperatura", -50), ("radiação", 2.5)))
        self.assertEqual(relatorio.contagem_leituras(), 2)

if __name__ == '__main__':
    unittest.main()