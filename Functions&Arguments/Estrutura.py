def calcular(a,b):
    return a + b

#Def instancia a função. a, b são os argumentos/parametros da função. Pode tb dizer sua tipagem. EX: 
def calcular(a: int, b: int):
    return a + b

#também podemos dizer a tipagem do return da função, EX:

def calcular(a: int, b: int) -> int:
    return a + b

# tipos tanto dos argumentos quanto do retorn podem ser: str, int, float, double, none etc



###    Estrutura Basica dos arquivos:

def main():
    name = get_name()
    greet(name)

def get_name():
    return input("Name: ")

def greet(name):
    print(f"Hello, {name}!")

main()