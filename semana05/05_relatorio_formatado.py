# Dados de exemplo para praticar listas e f-strings.
validos = ["Ana", "Gabriela"]
invalidos = ["Bruno", "Carla", "Diego", "Eva", "Felipe"]

total = len(validos) + len(invalidos)

# f-strings permitem inserir valores de variáveis no texto.
relatorio = f"""RELATÓRIO DE ANÁLISE
Total de registros: {total}
Válidos: {len(validos)}
Inválidos: {len(invalidos)}
Nomes válidos: {', '.join(validos)}
Nomes inválidos: {', '.join(invalidos)}
"""

# O modo w cria ou sobrescreve o arquivo de saída.
with open("relatorio_exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(relatorio)

print(relatorio)
