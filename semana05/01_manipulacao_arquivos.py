# Abre o CSV para leitura. O with fecha o arquivo automaticamente.
with open("dados.csv", "r", encoding="utf-8") as arquivo:
    # read() lê todo o conteúdo como uma string.
    conteudo = arquivo.read()

# Mostra o conteúdo do arquivo no terminal.
print(conteudo)
