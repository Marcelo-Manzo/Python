numero = int(input("numero: "))
count = numero
primo = False
while count > 1:
    if numero % count != 0 or count == numero:
        primo = True
    else:
        primo = False
    count -=1

if primo == False:
    print("não é primo")
else:
    print("é primo")

