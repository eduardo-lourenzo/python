from datetime import datetime

class Transacao:
    def __init__(self, descicao, valor, categoria, data):
        self.descricao = descicao
        self.valor = valor
        self.categoria = categoria
        self.data = datetime.strptime(data, "%d/%m/%Y")

    
    def resumo(self):
        return f"{self.descricao} | {self.valor:+,.2f} | {self.categoria} | {self.data.strftime('%d/%m/%Y')}"


def main():
    print("Controle Financeiro Pessoal")
    testeTrasacao = Transacao("Salário", +2500, "Renda", "10/04/2025")
    print(testeTrasacao.resumo())

if __name__ == "__main__":
    main()