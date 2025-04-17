class RoboExplorador:
    def __init__(self, nome: str, planeta_destino: str, energia: int):
        self.__nome = nome
        self.planeta_destino = planeta_destino
        self.__energia = energia
    
    def __str__(self) -> str:
        return f"Robô {self.__nome} - Destino: {self.planeta_destino} - Energia: {self.__energia}%"