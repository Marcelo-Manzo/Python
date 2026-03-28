def main():
    distancia = int(input())
    if 6 <= distancia <= 800008:
        CalcularPonto(distancia)


def CalcularPonto(distancia:int):
                        #3 do emissor + 2 da distancia ate o receptor
    ponto = (distancia-5)%8
    print(ponto)

main()
