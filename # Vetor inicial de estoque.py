# Vetor inicial de estoque
estoque = [20, 15, 10, 30, 5]

# Função para atualizar o estoque após uma venda
def vender(estoque, produto, quantidade):
    estoque[produto - 1] -= quantidade

# Função para adicionar unidades ao estoque
def adicionar(estoque, produto, quantidade):
    estoque[produto - 1] += quantidade

# Função para exibir o estoque atual
def exibir(estoque):
    print("Estoque atual:")
    for i in range(len(estoque)):
        print(f"Produto {i+1}: {estoque[i]} unidades")

# ----- Operações solicitadas -----

# Vendas
vender(estoque, 1, 3)  # vende 3 unidades do produto 1
vender(estoque, 4, 2)  # vende 2 unidades do produto 4

# Adição
adicionar(estoque, 5, 10)  # adiciona 10 unidades ao produto 5

# Exibir estoque atualizado
exibir(estoque)
