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

# Versão equivalente em Portugol (pseudocódigo), usando o método da bolha:
# algoritmo "ordenar_produtos_por_preco"
# var
#     nomes: vetor[1..3] de cadeia
#     precos: vetor[1..3] de real
#     categorias: vetor[1..3] de cadeia
#     nomes_copia: vetor[1..3] de cadeia
#     precos_copia: vetor[1..3] de real
#     categorias_copia: vetor[1..3] de cadeia
#     nomes_decrescentes: vetor[1..3] de cadeia
#     precos_decrescentes: vetor[1..3] de real
#     categorias_decrescentes: vetor[1..3] de cadeia
#     quantidade, i, passagem: inteiro
#     nome_temporario: cadeia
#     categoria_temporaria: cadeia
#     preco_temporario: real
# inicio
#     quantidade <- 3
#     nomes[1] <- "Caneta"
#     precos[1] <- 2.50
#     categorias[1] <- "Papelaria"
#     nomes[2] <- "Caderno"
#     precos[2] <- 15.00
#     categorias[2] <- "Papelaria"
#     nomes[3] <- "Borracha"
#     precos[3] <- 1.00
#     categorias[3] <- "Papelaria"
#
#     para i de 1 ate quantidade faca
#         nomes_copia[i] <- nomes[i]
#         precos_copia[i] <- precos[i]
#         categorias_copia[i] <- categorias[i]
#     fimpara
#
#     // Ordem crescente: compara vizinhos e troca se estiverem fora de ordem.
#     para passagem de 1 ate quantidade - 1 faca
#         para i de 1 ate quantidade - passagem faca
#             se precos_copia[i] > precos_copia[i + 1] entao
#                 preco_temporario <- precos_copia[i]
#                 precos_copia[i] <- precos_copia[i + 1]
#                 precos_copia[i + 1] <- preco_temporario
#                 nome_temporario <- nomes_copia[i]
#                 nomes_copia[i] <- nomes_copia[i + 1]
#                 nomes_copia[i + 1] <- nome_temporario
#                 categoria_temporaria <- categorias_copia[i]
#                 categorias_copia[i] <- categorias_copia[i + 1]
#                 categorias_copia[i + 1] <- categoria_temporaria
#             fimse
#         fimpara
#     fimpara
#     para i de 1 ate quantidade faca
#         escreva(nomes_copia[i], " - ", precos_copia[i], " - ",
#                 categorias_copia[i])
#     fimpara
#
#     para i de 1 ate quantidade faca
#         nomes_decrescentes[i] <- nomes[i]
#         precos_decrescentes[i] <- precos[i]
#         categorias_decrescentes[i] <- categorias[i]
#     fimpara
#     para passagem de 1 ate quantidade - 1 faca
#         para i de 1 ate quantidade - passagem faca
#             se precos_decrescentes[i] < precos_decrescentes[i + 1] entao
#                 preco_temporario <- precos_decrescentes[i]
#                 precos_decrescentes[i] <- precos_decrescentes[i + 1]
#                 precos_decrescentes[i + 1] <- preco_temporario
#                 nome_temporario <- nomes_decrescentes[i]
#                 nomes_decrescentes[i] <- nomes_decrescentes[i + 1]
#                 nomes_decrescentes[i + 1] <- nome_temporario
#                 categoria_temporaria <- categorias_decrescentes[i]
#                 categorias_decrescentes[i] <- categorias_decrescentes[i + 1]
#                 categorias_decrescentes[i + 1] <- categoria_temporaria
#             fimse
#         fimpara
#     fimpara
#     para i de 1 ate quantidade faca
#         escreva(nomes_decrescentes[i], " - ", precos_decrescentes[i], " - ",
#                 categorias_decrescentes[i])
#     fimpara
# fimalgoritmo