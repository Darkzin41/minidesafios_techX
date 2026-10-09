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