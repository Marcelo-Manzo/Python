tabuada = int(input("digite o numero da tabuada: "))
Dist = int(input("até qual numero: "))
Resultado = None

for i in range (Dist):
    Resultado = (i+1) * tabuada
    print(f"{tabuada}x{i+1} = {Resultado}")
    

