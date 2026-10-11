# Em Python, o with é uma estrutura utilizada para gerenciar recursos automaticamente, garantindo que eles sejam liberados corretamente após o uso, mesmo que aconteça algum erro durante a execução.
# Ele é muito utilizado na manipulação de arquivos, mas também pode ser aplicado em conexões com bancos de dados, gerenciamento de locks e outros recursos.

with open("dados.csv", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)