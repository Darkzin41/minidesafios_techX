import csv  # Permite ler as colunas e as linhas do CSV.

try:
    # O código dentro de try pode gerar uma exceção.
    with open("dados.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)  # Cada linha vira um dicionário.
        for pessoa in leitor:
            idade = int(pessoa["idade"])  # Pode gerar ValueError.
            print(f"{pessoa['nome']}: {idade} anos")

except FileNotFoundError:
    print("Erro: o arquivo dados.csv não foi encontrado.")
except KeyError:
    print("Erro: coluna nome ou idade não encontrada no CSV.")
except ValueError:
    print("Erro: idade não é um número válido.")
else:
    # Executa somente se nenhum erro ocorreu no try.
    print("Leitura realizada com sucesso.")
finally:
    # Executa tanto em caso de erro quanto de sucesso.
    print("Fim da leitura.")
