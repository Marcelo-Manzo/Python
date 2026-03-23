def main():
    nome = str(input("nome: "))
    SepararIniciais(nome)


# o meu: 
# def SepararIniciais(nome: str):
#     iniciais = ""
#     for i in range(len(nome)):
#         if nome[i] == " " or nome[i] == None:
#             iniciais += nome[i+1].upper() + "."
#     print(iniciais)
#     return iniciais



def SepararIniciais(nome: str):
    # .split() quebra a string em uma lista, ignorando espaços extras
    # O .split() transforma uma string em uma LISTA de palavras.
# 1. Sem argumentos: ele remove espaços extras no início, no fim e entre palavras.
# Exemplo: "  pedro   joao  ".split() -> ['pedro', 'joao']

# 2. Com argumento: você define onde cortar.
# Exemplo: "10/05/2024".split("/") -> ['10', '05', '2024']

    palavras = []
    palavras = nome.split() 
    iniciais = ""
    
    for p in palavras:
        # Pega a primeira letra de cada palavra
        iniciais += p[0].upper() + "."
        
    print(iniciais)
    return iniciais

main()



