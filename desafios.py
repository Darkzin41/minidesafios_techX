#Parte 1 
#calculadora de troco
valor_compra = float(input("Valor da compra: "))
valor_pago = float(input("Valor que foi pago: "))
troco = valor_pago - valor_compra
print(f"Valor do troco é equivalente a {troco:.2f}")

#conversor de tempo
segundos =  int(input("Digite em segundos inteiros: "))
conversao_horas = segundos // 3600
conversao_minutos = (segundos % 3600) // 60
conversao_segundos = segundos % 60
print(f"{segundos} segundos equivalem a {conversao_horas:.1f} horas, {conversao_minutos} minutos e {conversao_segundos} segundos")

#par ou impar
numero = int(input("Digite um numero inteiro: "))
par = numero % 2 == 0
impar = numero % 2 != 0
if par: 
    print(f"o numero {numero} é par")
else: 
    print(f"o numero {numero} é impar")

#parte 2 
# Media de notas 
nota1, nota2, nota3 = map(float, input("Digite as 3 notas do aluno: ").split())
media = (nota1 + nota2 + nota3)/3
print(f"A media deste aluno é equivalente a {media:.2f}")

#versao com com condicionais 
nota1, nota2, nota3 = map(float, input("Digite as 3 notas do aluno: ").split())
notas = [nota1, nota2, nota3]
media = media = sum(notas) / len(notas)
if media >= 9.0:
    print("Aluno aprovado com louvor")

elif media >= 7.0:
    print("Aluno aprovado")

else:
    print("Aluno reprovado")

#calculadora de desconto
valor, desconto = map(float, input("Digite o preço do produto e o percentual do desconto que ganhou: ").split())
valor_desconto = valor * (desconto/100)
valor_final = valor - valor_desconto
print(f"O valor final com o desconto ganho é equivalente a {valor_final:.2f}")

#inversor de nome 
nome = input("Digite seu nome completo: ")
nome_invertido = nome[::-1]
print(f"O nome invertido é {nome_invertido}")