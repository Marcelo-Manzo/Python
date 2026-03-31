def main():
    codigo = input("codigo: ") # Input já vem como string
    cartasEspacadas = codigo
    if 3 <= len(codigo) <= 156:
        # Cria uma lista pegando de 3 em 3 caracteres
        cartasEspacadas = " ".join([codigo[i:i+3] for i in range(0, len(codigo), 3)])
        #11P 01C 02C 01U 02U 03U 04U 
    cartas = cartasEspacadas.split()
    #['11P', '01C', '02C', '01U', '02U', '03U', '04U']
    Verificar(cartas)


def Verificar(cartas):
    copas = []
    espadas = []
    ouros = []
    paus = []

    for codigo in cartas:
        #01C codigo[2] = C
        match codigo[2]:
                case "C":
                    copas.append(codigo)
                case "E":
                    espadas.append(codigo)
                case "U":
                    ouros.append(codigo)
                case "P":
                    paus.append(codigo)

    for i in [copas, espadas, ouros, paus]:

        maiorCarta = 0

        for numero in i:
            carta = "".join([c for c in numero if c.isdigit()])
            if int(carta) > maiorCarta:
                maiorCarta = int(carta)
        if maiorCarta == 13:
            print("0")
        else:
            cartasFaltando = 13 - maiorCarta
            print(cartasFaltando)



main()
        

    

#[11P 01C, 02C ,01U ,02U ,03U ,04U]
