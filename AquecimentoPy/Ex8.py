lista = []
pares = 0
for i in range(10):
    var = int(input("numero: "))
    lista.append(var)
    if(var%2 == 0):
        pares += 1

print(lista)
print(f"pares: {pares}")
    

