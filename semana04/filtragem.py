# Filtragem por Preço: Uma funcionalidade que liste apenas os produtos que custam acima (ou abaixo) de um valor informado pelo usuário.

# lista de produtos para teste 
produtos = [
    ("Caneta", 2.50, "Papelaria"),
    ("Caderno", 15.00, "Papelaria"),
]

# input dos valores
valor, preco_max, preco_min = [float(x.strip()) for x in input("Digite o valor para filtrar, o valor maximo e o valor minimo separados por vírgula: ").split(",")]

# funcao
def filtrar_por_preco(produtos, preco_min, preco_max):
    # linha simplificada para filtrar produtos por preço usando list comprehension - primeiro um loop em seguida um condicional para garantir que o preço do produto esteja dentro do intervalo definido pelo usuário
    return [produto for produto in produtos if produto[1] >= preco_min and produto[1] <= preco_max]

print(f"Produtos filtrados por preço entre {preco_min} e {preco_max}: {filtrar_por_preco(produtos, preco_min, preco_max)}")

