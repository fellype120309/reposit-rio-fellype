def __init__(self, numero_conta, saldo=0):
    self.numero_conta = numero_conta
    self.saldo = saldo
    self.transacoes = []
def depositar(self, valor):
    self.saldo += valor
    self.registrar_transacao("Depósito", valor)
def sacar(self, valor):
    if self.saldo >= valor:
        self.saldo -= valor
        self.registrar_transacao("Saque", valor)
    else:
        print("Saldo insuficiente.")