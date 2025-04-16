from datetime import datetime

class Transacao:
    def __init__(self, descricao, valor, categoria, data):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = datetime.strptime(data, "%d/%m/%Y")
    
    def resumo(self):
        return f"{self.descricao} | {self.valor:+,.2f} | {self.categoria} | {self.data.strftime('%d/%m/%Y')}"


class Carteira:
    def __init__(self):
        self.lista_de_transacoes = list()
    
    def adicionar (self, transacao: Transacao):
        self.lista_de_transacoes.append(transacao)
    
    def exibir_transacoes(self):
        for transacao in self.lista_de_transacoes:
            print(transacao.resumo())

    def saldo(self) -> float:
        return sum(transacao.valor for transacao in self.lista_de_transacoes)
    
    def filtrar_por_categoria(self, categoria: str):
        for transacao in self.lista_de_transacoes:
            if transacao.categoria == categoria:
                print(transacao.resumo())

    def gastos_totais(self) -> float:
        totais = 0.0
        for transacao in self.lista_de_transacoes:
            if transacao.valor < 0.0:
                totais += transacao.valor
        return totais
    
    def renda_total(self) -> float:
        total = 0.0
        for transacao in self.lista_de_transacoes:
            if transacao.valor > 0.0:
                total += transacao.valor
        return total
    
    def resumo_geral(self):
        print(f"Total de transações: {len(self.lista_de_transacoes)}")
        print(f"Renda total: {self.renda_total():+.2f}")
        print(f"Gastos totais: {self.gastos_totais():.2f}")
        print(f"Saldo final: {self.saldo():+.2f}")


def main():
    pass

if __name__ == "__main__":
    main()