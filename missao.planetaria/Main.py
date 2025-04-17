from RelatorioDeMissao import RelatorioDeMissao

class main():
    lista_de_missoes = [
        RelatorioDeMissao("Spirit", "Marte", 85, (("temperatura", -50), ("radiação", 2.5))),
        RelatorioDeMissao("Opportunity", "Marte", 90, (("temperatura", -45), ("radiação", 3.0))),
        RelatorioDeMissao("Curiosity", "Marte", 75, (("temperatura", -60), ("radiação", 1.8))),
        RelatorioDeMissao("Perseverance", "Marte", 95, (("temperatura", -55), ("radiação", 2.2))),
        RelatorioDeMissao("Voyager 1", "Espaço Interestelar", 60, (("temperatura", -200), ("radiação", 0.5))),
        RelatorioDeMissao("Voyager 2", "Espaço Interestelar", 65, (("temperatura", -195), ("radiação", 0.7))),
        RelatorioDeMissao("Pioneer 10", "Espaço Interestelar", 50, (("temperatura", -210), ("radiação", 0.3))),
        RelatorioDeMissao("Pioneer 11", "Espaço Interestelar", 55, (("temperatura", -205), ("radiação", 0.4))),
        RelatorioDeMissao("Sojourner", "Marte", 70, (("temperatura", -65), ("radiação", 2.0))),
        RelatorioDeMissao("Luna 2", "Lua", 80, (("temperatura", -20), ("radiação", 5.0)))
        ]
    
    for missao in lista_de_missoes:
        print(f"{missao}: {missao.resumo()}")
        
if __name__ == "__main__":
    main()