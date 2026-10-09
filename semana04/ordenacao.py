# Ordenação: Exibição dos produtos por preço crescente (sort()) e decrescente (sorted(..., reverse=True)).

# lista de tuplas
produtos = [
    ("Caneta", 2.50, "Papelaria"),
    ("Caderno", 15.00, "Papelaria"),
    ("Borracha", 1.00, "Papelaria")
]

# A função sorted() percorre os itens de produtos e cria uma nova lista ordenada. O argumento key diz qual valor deve ser usado na comparação
produtos_crescentes = sorted(produtos, key=lambda p: p[1])
produtos_decrescentes = sorted(produtos, key=lambda p: p[1], reverse=True)

print(f"Produtos ordenados por preço crescente: {produtos_crescentes}")
print(f"Produtos ordenados por preço decrescente: {produtos_decrescentes}")