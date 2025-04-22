import unittest
from RoboExplorador import RoboExplorador

class TestRoboExplorador(unittest.TestCase):
    def test_robo_explorador(self):
        robo = RoboExplorador("Spirit", "Marte", 85)
        self.assertEqual(str(robo), "Robô Spirit - Destino: Marte - Energia: 85%")

if __name__ == '__main__':
    unittest.main()