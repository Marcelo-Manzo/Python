nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
nota3 = float(input("nota 3: "))

if nota1 > 10 or nota2 > 10 or nota3 > 10:
    print("notas invalidas")
else:
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        print("aprovado")
    elif media >= 5:
        print("recuperação")
    else:
        print("reprovado")

