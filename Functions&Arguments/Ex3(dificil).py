def main():
    text = str(input("texto: "))
    caesar_cipher(text)

def caesar_cipher(text, shift=3):
    text = ""
    for i in text:
        if i.isdigit():
            continue
        else:
            posicao = ord(nova_letra) - ord(i)
            nova_posicao = (posicao + shift) % 26
            nova_letra = chr(nova_posicao + ord(i))
    print(text)
    return text

main()