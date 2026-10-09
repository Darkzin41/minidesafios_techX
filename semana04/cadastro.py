produtos = []

nome, preco, categoria = input("Digite o nome do produto, preço e categoria separados por vírgula: ").split(",")

# nome = input("Digite o nome do produto: ")
# preco = float(input("Digite o preço do produto: "))
# categoria = input("Digite a categoria do produto: ")
preco = float(preco.strip())
produtos.append((nome, preco, categoria))
print(f"Produto cadastrado com sucesso!\n{produtos}")

# Versão equivalente em Portugol (pseudocódigo):
# algoritmo "cadastro_de_produto"
# var
#     nomes: vetor[1..100] de cadeia
#     precos: vetor[1..100] de real
#     categorias: vetor[1..100] de cadeia
#     quantidade, i: inteiro
# inicio
#     quantidade <- 1
#     escreva("Digite o nome, o preço e a categoria do produto:")
#     leia(nomes[1], precos[1], categorias[1])
#
#     escreva("Produto cadastrado:")
#     para i de 1 ate quantidade faca
#         escreva(nomes[i], " - ", precos[i], " - ", categorias[i])
#     fimpara
# fimalgoritmo