# Conjunto de Categorias Únicas: Criação de um set() com as categorias dos produtos, eliminando automaticamente as duplicatas.]

# lista de tuplas para pecorrer
produtos = [
    ("Caneta", 2.50, "Papelaria"),
    ("Cordão", 15.00, "Acessórios"),
    ("Caderno", 1.00, "Papelaria"),
]

# atribuindo a funcao set em categorias pecorrendo o indice dois das tuplas e pecorrendo-as. 
# Atribuindo a funcao set() para eliminar duplicatas e criar um conjunto de categorias únicas.
categorias = set(produto[2] for produto in produtos)

print(f"Categorias: {categorias}") #vai retornar papelaria uma vez e acessorios.

# Versão equivalente em Portugol (pseudocódigo), simulando o conjunto manualmente:
# algoritmo "categorias_sem_repeticao"
# var
#     categorias: vetor[1..3] de cadeia
#     categorias_unicas: vetor[1..3] de cadeia
#     quantidade, quantidade_unicas, i, j: inteiro
#     encontrada: logico
# inicio
#     quantidade <- 3
#     categorias[1] <- "Papelaria"
#     categorias[2] <- "Acessórios"
#     categorias[3] <- "Papelaria"
#     quantidade_unicas <- 0
#
#     para i de 1 ate quantidade faca
#         encontrada <- falso
#         para j de 1 ate quantidade_unicas faca
#             se categorias[i] = categorias_unicas[j] entao
#                 encontrada <- verdadeiro
#             fimse
#         fimpara
#
#         se encontrada = falso entao
#             quantidade_unicas <- quantidade_unicas + 1
#             categorias_unicas[quantidade_unicas] <- categorias[i]
#         fimse
#     fimpara
#
#     para i de 1 ate quantidade_unicas faca
#         escreva(categorias_unicas[i])
#     fimpara
# fimalgoritmo