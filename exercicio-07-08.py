##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2024
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: exercicios3\capitulo 07\exercicio-07-08.py
##############################################################################

palavras = [
          "casa",
          "bola",
          "mangueira",
          "uva",
          "quiabo",
          "computador",
          "cobra",
          "lentilha",
          "arroz"
     ]

indice = int(input("Digite um numero:"))
palavra = palavras[(indice * 776) % len(palavras)]
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = r"  |   "
    elif erros == 3:
        linha2 = r" \|   "
    elif erros >= 4:
        linha2 = r" \|/ "
    print(f"X{linha2}")
    linha3 = ""
    if erros == 5:
        linha3 += r" /     "
    elif erros >= 6:
        linha3 += r" / \ "
    print(f"X{linha3}")
    print("X\n===========")
    if erros == 6:
        print("Enforcado!")
        print(f"A palavra secreta era: {palavra}")
        break
