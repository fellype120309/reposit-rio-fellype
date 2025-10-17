# Vetor de estoque inicial
estoque = [20, 15, 10, 30, 5]

# Função para atualizar o estoque após uma venda
def vender(estoque, produto, quantidade):
    if 0 < produto <= len(estoque):
        if estoque[produto - 1] >= quantidade:
            estoque[produto - 1] -= quantidade
            print(f"Venda realizada: {quantidade} unidades do produto {produto}.")
        else:
            print(f"Estoque insuficiente para o produto {produto}.")
    else:
        print("Produto inválido.")

# Função para adicionar unidades ao estoque
def adicionar(estoque, produto, quantidade):
    if 0 < produto <= len(estoque):
        estoque[produto - 1] += quantidade
        print(f"Foram adicionadas {quantidade} unidades ao produto {produto}.")
    else:
        print("Produto inválido.")

# Função para exibir o estoque atual
def exibir_estoque(estoque):
    print("\n--- Estoque Atual ---")
    for i, quantidade in enumerate(estoque, start=1):
        print(f"Produto {i}: {quantidade} unidades")

# Operações solicitadas
vender(estoque, 1, 3)   # Vende 3 unidades do produto 1
vender(estoque, 4, 2)   # Vende 2 unidades do produto 4
adicionar(estoque, 5, 10)  # Adiciona 10 unidades ao produto 5

# Exibe o estoque atualizado
exibir_estoque(estoque)
