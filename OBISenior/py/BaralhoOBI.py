def main():
    codigo = input()

    #11P 01C 02C 01U 02U 03U 04U

    if 3 <= len(codigo) <= 156:
        # Ao invés de list comprehension, faz o fatiamento no for
        cartas = []
        for i in range(0, len(codigo), 3):
            carta = codigo[i:i+3]
            cartas.append(carta)

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

    naipes = [copas, espadas, ouros, paus]

    for naipe in naipes:

        # Extrai os números de cada carta do naipe
        numeros = []
        for carta in naipe:
            numero = int(carta[:2])
            numeros.append(numero)

        # Transforma em set para remover duplicatas
        numeros_sem_duplicata = set(numeros)

        # Se o tamanho mudou, tinha número repetido
        if len(numeros) != len(numeros_sem_duplicata):
            print("erro")
        else:
            faltando = 13 - len(numeros)
            print(faltando)


main()