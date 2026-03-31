def main():
    codigo = input()

    if 3 <= len(codigo) <= 156:
        cartas = [codigo[i:i+3] for i in range(0, len(codigo), 3)]
        verificar(cartas)


def verificar(cartas):
    copas = []
    espadas = []
    ouros = []
    paus = []

    for carta in cartas:
        match carta[2]:
            case "C":
                copas.append(carta)
            case "E":
                espadas.append(carta)
            case "U":
                ouros.append(carta)
            case "P":
                paus.append(carta)

    for naipe in [copas, espadas, ouros, paus]:
        numeros = [int(carta[:2]) for carta in naipe]

        # verifica duplicata
        if len(numeros) != len(set(numeros)):
            print("erro")
        else:
            faltando = 13 - len(numeros)
            print(faltando)


main()