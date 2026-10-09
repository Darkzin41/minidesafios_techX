produtos = []

nome, preco, categoria = input("Digite o nome do produto, preço e categoria separados por vírgula: ").split(",")

# nome = input("Digite o nome do produto: ")
# preco = float(input("Digite o preço do produto: "))
# categoria = input("Digite a categoria do produto: ")
preco = float(preco.strip())
produtos.append((nome, preco, categoria))
print(f"Produto cadastrado com sucesso!\n{produtos}")