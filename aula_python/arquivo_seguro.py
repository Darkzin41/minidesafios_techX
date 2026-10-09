try:
  with open("nao_existe.txt", "r") as f:
    conteudo = f.read()
    print("Arquivo encontrado!")
except FileNotFoundError:
  print("Arquivo não encontrado")
except PermissionError:
  print("Sem permissão para ler o arquivo ")