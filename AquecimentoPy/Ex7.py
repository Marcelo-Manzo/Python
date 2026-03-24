lista = []

for i in range (10):
    var = int(input("Numero: "))
    lista.append (var)
print(lista) 

maior = lista[0]
menor = lista[0]

for i in lista:
    if i > maior: 
        maior = i
    if i < menor:
        menor = i

print(f"maior: {maior}    menor: {menor}")