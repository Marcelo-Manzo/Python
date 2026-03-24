num1 = int(input("digite o 1° numero:"))
num2 = int(input("digite o 2° numero:"))
num3 = int(input("digite o 3° numero:"))

lista = [num1, num2, num3]
maior = lista[0]

for i in lista:
    if i > maior:
        maior = i

print(maior)

# ou
maior = None
for i in range(3):
    var = int(input(f"digite o {i}°: "))
    if var > maior:
        maior = var
        




