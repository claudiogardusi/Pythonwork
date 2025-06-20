"""
Lista 3 Exercício 1
"""
import random as rd

numero = rd.randint(1, 200)

for i in range(10):
    resposta = input('Digite um número ---> ')
    if int(resposta) == int(numero):
        print('Valeu você acertou!!!')
        break
    elif int(resposta) < int(numero):
        print('Errado! O número é maior!')
        print('Tentativa ', i + 1)
        if i + 1 == 10:
            print('Acabaram as suas tentativas')
    elif int(resposta) > int(numero):
        print('Errado! O número é menor!')
        print('Tentativa ', i + 1)
        if i + 1 == 10:
            print('Acabaram as suas tentativas')
print('O número gerado foi - ', numero)
