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

# Versão equivalente em Portugol (pseudocódigo):
# algoritmo "filtrar_produtos_por_preco"
# var
#     nomes: vetor[1..2] de cadeia
#     precos: vetor[1..2] de real
#     categorias: vetor[1..2] de cadeia
#     nomes_filtrados: vetor[1..2] de cadeia
#     precos_filtrados: vetor[1..2] de real
#     categorias_filtradas: vetor[1..2] de cadeia
#     quantidade, quantidade_filtrada, i: inteiro
#     preco_minimo, preco_maximo: real
# inicio
#     quantidade <- 2
#     nomes[1] <- "Caneta"
#     precos[1] <- 2.50
#     categorias[1] <- "Papelaria"
#     nomes[2] <- "Caderno"
#     precos[2] <- 15.00
#     categorias[2] <- "Papelaria"
#
#     escreva("Digite o preço mínimo e o preço máximo:")
#     leia(preco_minimo, preco_maximo)
#     quantidade_filtrada <- 0
#
#     para i de 1 ate quantidade faca
#         se precos[i] >= preco_minimo e precos[i] <= preco_maximo entao
#             quantidade_filtrada <- quantidade_filtrada + 1
#             nomes_filtrados[quantidade_filtrada] <- nomes[i]
#             precos_filtrados[quantidade_filtrada] <- precos[i]
#             categorias_filtradas[quantidade_filtrada] <- categorias[i]
#         fimse
#     fimpara
#
#     para i de 1 ate quantidade_filtrada faca
#         escreva(nomes_filtrados[i], " - ", precos_filtrados[i],
#                 " - ", categorias_filtradas[i])
#     fimpara
# fimalgoritmo
