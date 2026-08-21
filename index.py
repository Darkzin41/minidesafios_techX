# Calculadora de IMC 
peso = float(input("peso (kg):"))
altura = float(input("altura (m):"))
imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")

# # Conversor de moedas
valor_reais = float(input("Valor em R$: "))
cotacao_dolar = 5.10
valor_dolar = valor_reais/cotacao_dolar
print(f"R$ {valor_reais} = US$ {valor_dolar:.2f}")

# #Conversor de Temperatura
celsius = float(input("Temperatura em °C: "))
fahrenheit = celsius * (9/5) + 32
kelvin = celsius + 273.15
print(f"{celsius}°C  = {fahrenheit:.1f}°F = {kelvin:.1f}K ")

#Area e perimetro de um retangulo 
base = float(input("Digite o comprimento/base do retangulo: "))
altura = float(input("Digite a altura h/largura do retangulo: "))
area = base * altura
perimetro = 2 * (base + altura)
print(f"A area do retangulo é igual a {area:.2f} m² e o perimetro é igual a {perimetro:.2f} m")

#Nome completo 
nome = input("Primeiro nome: ").strip().capitalize()
sobrenome = input("Sobrenome: ").strip().capitalize()
#aqui o strip é usado para remover espaços antes e depois do que foi digitado e elimina tambem elementos whitespace, já o capitalize deixa maiuscula a primeira letra da string e o resto em minusculo
completo = f"{nome} {sobrenome}"
print(f"Nome formatado = {completo}")
print(f"Iniciais: {nome[0]}.{sobrenome[0]}")

