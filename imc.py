""" 
Primeira lista de Exercícios - Exercicio  16
Faça um programa que realize o cadastro de um usuário a partir 
de seu nome, idade, peso, altura 
que deverão ser informados pelo usuário e exiba a frase: 
Seu nome ____ tem __ letras, 
você tem _ anos e nasceu no ano de ____. 
Você mede ___cm, pesa ___ Kg e seu IMC é:____. 
Não esqueça de manter uma boa interface com o usuário!! 
*Fórmula do cálculo do IMC: IMC = Peso ÷ (Altura × Altura)
"""
import datetime
hoje = datetime.date.today()
dia = hoje.day
mes = hoje.month
ano = hoje.year
nome = input('Olá, digite seu nome ')
idade = input(f'{nome} quantos anos você tem? (só numeros) ')
mesnasc = input(f'Há, em que mês você nasceu {nome}? Lembre-se só numeros!')
peso = input(f'Qual seu peso {nome}? (em kilos) ')
print(f'Qual a sua altura {nome}?')
altura = input('Digite em metros, exemplo "1.65", e não esquça de usar .(ponto)')
tnome = len(nome)
if int(mesnasc) > int(mes):
    idade = int(idade) + 1
anonasc = int(ano) - int(idade)
imc = float(peso) / (float(altura) ** 2)
print(f'Seu nome, {nome} tem {tnome} letras')
print(f'Como você tem {str(idade)} nasceu no mê {str(mesnasc)} então é de {str(anonasc)}')
print(f'Como você mede {str(altura)}  e pesa {str(peso)} kilos Seu IMC é {str(round(imc,2))}')