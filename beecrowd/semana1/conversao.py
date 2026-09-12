N = float(input("Digite o valor em segundos: "))
horas = N // 3600
minutos = (N % 3600) // 60
segundos = N % 60
print(f"{int(horas)}:{int(minutos)}:{int(segundos)}")

#divide o total de N segundos por 3600 para obter o numero de horas, depois pegao o resto dessa divisao e divide por 60 pra pegar o de minutos, e o resto dessa segunda divisao é os segundos restantes