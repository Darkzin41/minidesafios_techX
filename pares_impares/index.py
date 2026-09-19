import sys 

#substituindo o input,
#essa função é mais rapido que o input

n = int(sys.stdin.readline())

pares =[]
impares = []

for _ in range(n):
    number = int(sys.stdin.readline())
    if number%2==0:
        pares.append(number)
    else:
        impares.append(number)
        
pares.sort()
impares.sort(reverse=True)
    
for number in pares:
    print(number)
for number in impares:
    print(number)