from RoboExplorador import RoboExplorador

class RelatorioDeMissao(RoboExplorador):
    def __init__(self, nome: str, planeta_destino: str, energia: int, leituras: tuple):
        super().__init__(nome, planeta_destino, energia)
        self.__leituras = leituras
    
    def resumo(self) -> list:
        return [f"{nome}: {valor}" for nome, valor in self.__leituras]
    
    def contagem_leituras(self) -> int:
        return len(self.__leituras)
