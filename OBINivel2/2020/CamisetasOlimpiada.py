def main():
    premiados = int(input())
    tamanhosPremiados = str(input()).replace(" ", "")
    pequenas = int(input())
    medias = int(input()) 
    Verificar(premiados, tamanhosPremiados, pequenas, medias)

def Verificar(premiados, tamanhosPremiados, pequenas, medias):
    if premiados != len(tamanhosPremiados):
        print("N")
    
    qtdPequenas = 0
    qtdMedias = 0

    for i in tamanhosPremiados:
        if int(i) == 1:
            qtdPequenas+= 1
        if int(i) == 2:
            qtdMedias+= 1

    if qtdPequenas == pequenas and qtdMedias == medias:
        print("S")
    else:
        print("N")


main()