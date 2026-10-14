import csv
import re


# A regex verifica o formato do campo, como mostrado nos slides.
def validar_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))


def validar_cpf(cpf):
    return bool(re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf))


def validar_telefone(telefone):
    return bool(re.match(r"^\(\d{2}\)\s\d{4,5}-\d{4}$", telefone))


def validar_data(data):
    return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", data))


# Exceção usada quando um registro não segue uma regra de validação.
class FormatoInvalidoError(Exception):
    pass


validos = []
invalidos = []

try:
    # Abre o CSV com fechamento automático ao sair do with.
    with open("dados.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)  # Lê cada linha como dicionário.

        # Garante que as colunas necessárias existem no arquivo.
        for coluna in ["nome", "email", "cpf", "telefone", "data", "idade"]:
            if coluna not in (leitor.fieldnames or []):
                raise KeyError(coluna)

        for pessoa in leitor:
            nome = pessoa["nome"]
            try:
                # int() demonstra a conversão de tipos e pode gerar ValueError.
                idade = int(pessoa["idade"])

                # Cada campo precisa respeitar o formato definido na regex.
                if not validar_email(pessoa["email"]):
                    raise FormatoInvalidoError("e-mail inválido")
                if not validar_cpf(pessoa["cpf"]):
                    raise FormatoInvalidoError("CPF fora do formato")
                if not validar_telefone(pessoa["telefone"]):
                    raise FormatoInvalidoError("telefone fora do formato")
                if not validar_data(pessoa["data"]):
                    raise FormatoInvalidoError("data fora do formato")

                validos.append(f"{nome} ({idade} anos)")

            except (FormatoInvalidoError, ValueError) as erro:
                # Um registro inválido não impede a análise dos seguintes.
                invalidos.append(f"{nome}: {erro}")

except FileNotFoundError:
    print("Erro: arquivo dados.csv não encontrado.")
except KeyError as erro:
    print(f"Erro: coluna obrigatória ausente: {erro}")
else:
    # O else executa quando a leitura não encontrou os erros externos acima.
    total = len(validos) + len(invalidos)
    relatorio = f"""RELATÓRIO DE ANÁLISE DE DADOS
Total de registros: {total}
Válidos: {len(validos)}
Inválidos: {len(invalidos)}

REGISTROS VÁLIDOS:
"""

    for pessoa in validos:
        relatorio += f"- {pessoa}\n"

    relatorio += "\nREGISTROS INVÁLIDOS:\n"
    for pessoa in invalidos:
        relatorio += f"- {pessoa}\n"

    # Salva e apresenta o relatório final.
    with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)
    print(relatorio)
finally:
    print("Análise finalizada.")
