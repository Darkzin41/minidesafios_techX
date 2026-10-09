# Relatório final com os resultados das atividades da semana.

produtos = [
    ("Caneta", 2.50, "Papelaria"),
    ("Cordão", 15.00, "Acessórios"),
    ("Caderno", 1.00, "Papelaria"),
    ("Borracha", 1.00, "Papelaria"),
]

preco_min, preco_max = (
    float(valor.strip())
    for valor in input(
        "Digite o preço mínimo e o preço máximo separados por vírgula: "
    ).split(",")
)

produtos_crescentes = sorted(produtos, key=lambda produto: produto[1])
produtos_decrescentes = sorted(produtos, key=lambda produto: produto[1], reverse=True)
produtos_filtrados = [
    produto for produto in produtos if preco_min <= produto[1] <= preco_max
]

precos = [produto[1] for produto in produtos]
menor_preco = min(precos)
maior_preco = max(precos)
preco_medio = sum(precos) / len(precos)
categorias = sorted({produto[2] for produto in produtos})

print(f"\n{'=' * 40}")
print(f"{'RELATÓRIO DE PRODUTOS':^40}")
print(f"{'=' * 40}")

print(f"\nProdutos cadastrados ({len(produtos)}):")
for nome, preco, categoria in produtos:
    print(f"- {nome}: R$ {preco:.2f} | Categoria: {categoria}")

print("\nEstatísticas de preços:")
print(f"- Menor preço: R$ {menor_preco:.2f}")
print(f"- Maior preço: R$ {maior_preco:.2f}")
print(f"- Preço médio: R$ {preco_medio:.2f}")

print("\nProdutos por preço crescente:")
for nome, preco, _ in produtos_crescentes:
    print(f"- {nome}: R$ {preco:.2f}")

print("\nProdutos por preço decrescente:")
for nome, preco, _ in produtos_decrescentes:
    print(f"- {nome}: R$ {preco:.2f}")

print(f"\nCategorias únicas: {', '.join(categorias)}")
print(f"\nProdutos entre R$ {preco_min:.2f} e R$ {preco_max:.2f}:")
if produtos_filtrados:
    for nome, preco, categoria in produtos_filtrados:
        print(f"- {nome}: R$ {preco:.2f} | Categoria: {categoria}")
else:
    print("- Nenhum produto encontrado nessa faixa de preço.")

# Versão equivalente em Portugol (pseudocódigo):
# algoritmo "relatorio_de_produtos"
# var
#     nomes: vetor[1..4] de cadeia
#     precos: vetor[1..4] de real
#     categorias: vetor[1..4] de cadeia
#     nomes_ordenados: vetor[1..4] de cadeia
#     precos_ordenados: vetor[1..4] de real
#     nomes_decrescentes: vetor[1..4] de cadeia
#     precos_decrescentes: vetor[1..4] de real
#     categorias_unicas: vetor[1..4] de cadeia
#     quantidade, quantidade_unicas, i, j, passagem: inteiro
#     menor_preco, maior_preco, soma, media: real
#     preco_minimo, preco_maximo, temporario_preco: real
#     temporario_nome, temporaria_categoria: cadeia
#     encontrada: logico
# inicio
#     quantidade <- 4
#     nomes[1] <- "Caneta"
#     precos[1] <- 2.50
#     categorias[1] <- "Papelaria"
#     nomes[2] <- "Cordão"
#     precos[2] <- 15.00
#     categorias[2] <- "Acessórios"
#     nomes[3] <- "Caderno"
#     precos[3] <- 1.00
#     categorias[3] <- "Papelaria"
#     nomes[4] <- "Borracha"
#     precos[4] <- 1.00
#     categorias[4] <- "Papelaria"
#
#     escreva("Digite o preço mínimo e o preço máximo:")
#     leia(preco_minimo, preco_maximo)
#
#     menor_preco <- precos[1]
#     maior_preco <- precos[1]
#     soma <- 0
#     quantidade_unicas <- 0
#     para i de 1 ate quantidade faca
#         se precos[i] < menor_preco entao
#             menor_preco <- precos[i]
#         fimse
#         se precos[i] > maior_preco entao
#             maior_preco <- precos[i]
#         fimse
#         soma <- soma + precos[i]
#
#         // Simula um conjunto: só guarda a categoria se ainda não existir.
#         encontrada <- falso
#         para j de 1 ate quantidade_unicas faca
#             se categorias[i] = categorias_unicas[j] entao
#                 encontrada <- verdadeiro
#             fimse
#         fimpara
#         se encontrada = falso entao
#             quantidade_unicas <- quantidade_unicas + 1
#             categorias_unicas[quantidade_unicas] <- categorias[i]
#         fimse
#     fimpara
#     media <- soma / quantidade
#
#     // Ordena cópias por preço crescente com o método da bolha.
#     para i de 1 ate quantidade faca
#         nomes_ordenados[i] <- nomes[i]
#         precos_ordenados[i] <- precos[i]
#     fimpara
#     para passagem de 1 ate quantidade - 1 faca
#         para i de 1 ate quantidade - passagem faca
#             se precos_ordenados[i] > precos_ordenados[i + 1] entao
#                 temporario_preco <- precos_ordenados[i]
#                 precos_ordenados[i] <- precos_ordenados[i + 1]
#                 precos_ordenados[i + 1] <- temporario_preco
#                 temporario_nome <- nomes_ordenados[i]
#                 nomes_ordenados[i] <- nomes_ordenados[i + 1]
#                 nomes_ordenados[i + 1] <- temporario_nome
#             fimse
#         fimpara
#     fimpara
#     para i de 1 ate quantidade faca
#         nomes_decrescentes[i] <- nomes[i]
#         precos_decrescentes[i] <- precos[i]
#     fimpara
#     para passagem de 1 ate quantidade - 1 faca
#         para i de 1 ate quantidade - passagem faca
#             se precos_decrescentes[i] < precos_decrescentes[i + 1] entao
#                 temporario_preco <- precos_decrescentes[i]
#                 precos_decrescentes[i] <- precos_decrescentes[i + 1]
#                 precos_decrescentes[i + 1] <- temporario_preco
#                 temporario_nome <- nomes_decrescentes[i]
#                 nomes_decrescentes[i] <- nomes_decrescentes[i + 1]
#                 nomes_decrescentes[i + 1] <- temporario_nome
#             fimse
#         fimpara
#     fimpara
#
#     escreva("Produtos cadastrados: ", quantidade)
#     para i de 1 ate quantidade faca
#         escreva(nomes[i], " - ", precos[i], " - ", categorias[i])
#     fimpara
#     escreva("Menor preço: ", menor_preco, " | Maior preço: ", maior_preco)
#     escreva("Preço médio: ", media)
#     escreva("Produtos por preço crescente:")
#     para i de 1 ate quantidade faca
#         escreva(nomes_ordenados[i], " - ", precos_ordenados[i])
#     fimpara
#     escreva("Produtos por preço decrescente:")
#     para i de 1 ate quantidade faca
#         escreva(nomes_decrescentes[i], " - ", precos_decrescentes[i])
#     fimpara
#     escreva("Categorias únicas:")
#     para i de 1 ate quantidade_unicas faca
#         escreva(categorias_unicas[i])
#     fimpara
#     escreva("Produtos na faixa informada:")
#     para i de 1 ate quantidade faca
#         se precos[i] >= preco_minimo e precos[i] <= preco_maximo entao
#             escreva(nomes[i], " - ", precos[i], " - ", categorias[i])
#         fimse
#     fimpara
# fimalgoritmo