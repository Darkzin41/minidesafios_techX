# with open("dados.txt", "r", encoding="utf-8") as f:
#           conteudo = f.read()
#           print(conteudo)

# import csv

# # Leitura
# with open("dados.csv", "r", encoding="utf-8") as f:
#     leitor = csv.reader(f)
#     for linha in leitor:
#         print(linha)

# # Escrita
# with open("saida.csv", "w", encoding="utf-8", newline="") as f:
#     escritor = csv.writer(f)
#     escritor.writerow(["nome", "idade"])
#     escritor.writerow(["Ana", 25])
#     escritor.writerow(["Bruno", 30])


#json
import json

# Leitura
# with open("dados.json", "r", encoding="utf-8") as f:
#     dados = json.load(f)
#     print(dados)

# Escrita
dados = {"nome": "Ana", "idade": 25}

with open("saida.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)