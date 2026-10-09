# Tupla de Estatísticas: Criação de uma tupla imutável contendo o menor preço (min()), o maior preço (max()) e a média dos preços (sum() / len()).

# lista de produtos para teste
produtos = [
    ("Caneta", 2.50),
    ("Cordão", 15.00),
    ("Caderno", 1.00),
    ("Borracha", 1.00)
]

# Criando a tupla de estatísticas (mesma ideia das anteriores, atribuo uma funcao e pecorro com list comprehension para pecorrer o indice 1 das tuplas e pecorrer as tuplas - funcao min (valor minimo), funcao max (valor maximo) e funcao sum (soma dos valores) dividida pelo tamanho da lista de produtos para calcular a media com len(produtos))
estatisticas = (min(produto[1] for produto in produtos), max(produto[1] for produto in produtos), sum(produto[1] for produto in produtos) / len(produtos))

print(f"Estatísticas: Menor preço: {estatisticas[0]}, Maior preço: {estatisticas[1]}, Média: {estatisticas[2]}")