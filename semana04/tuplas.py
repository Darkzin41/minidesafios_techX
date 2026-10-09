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

# Versão equivalente em Portugol (pseudocódigo):
# algoritmo "estatisticas_de_precos"
# var
#     nomes: vetor[1..4] de cadeia
#     precos: vetor[1..4] de real
#     quantidade, i: inteiro
#     menor_preco, maior_preco, soma, media: real
# inicio
#     quantidade <- 4
#     nomes[1] <- "Caneta"
#     precos[1] <- 2.50
#     nomes[2] <- "Cordão"
#     precos[2] <- 15.00
#     nomes[3] <- "Caderno"
#     precos[3] <- 1.00
#     nomes[4] <- "Borracha"
#     precos[4] <- 1.00
#
#     menor_preco <- precos[1]
#     maior_preco <- precos[1]
#     soma <- 0
#     para i de 1 ate quantidade faca
#         se precos[i] < menor_preco entao
#             menor_preco <- precos[i]
#         fimse
#         se precos[i] > maior_preco entao
#             maior_preco <- precos[i]
#         fimse
#         soma <- soma + precos[i]
#     fimpara
#     media <- soma / quantidade
#
#     escreva("Menor preço: ", menor_preco)
#     escreva("Maior preço: ", maior_preco)
#     escreva("Preço médio: ", media)
# fimalgoritmo