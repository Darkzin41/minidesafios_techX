print("=== Menu de inscrição da Maratona 2026 ===")

print("1 - Maratona de Completa")
print("2 - Meia Maratona" )
print("3 - Corrida de Estreia" )
  


opcao = int(input("Escolha o numero correspondente a sua categoria: "))

print(f"\n--- Resultado --- ")

match opcao:
    case 1:
        print("Inscrição Confirmada: Maratona Completa - 42km")
    case 2: 
        print("Inscrição Confirmada: Meia Maratona - 21km")
    case 3:
        print("Inscrição Confirmada: Corrida de Estreia - 5km")
    case _: 
       #"_" substitui o "caso contrario" - tipo um else]
       print("Erro: Categoria inexistente, escolha de 1 a 3")
