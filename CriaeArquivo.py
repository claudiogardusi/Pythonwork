
import os

nome_arquivo = "palavras.txt"

while True:
    palavra = input("Digite uma palavra (ou digite 'sair' para terminar): ")
    if palavra == "sair":
        break
    # Armazenar a palavra no arquivo
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write(palavra + "\n")

arquivo.close()

"""
**********

def salvar_palavras_csv(palavras, nome_arquivo):
  """
  Função para salvar uma lista de palavras em um arquivo CSV.

  Argumentos:
    palavras: Uma lista de strings representando as palavras a serem salvas.
    nome_arquivo: O nome do arquivo CSV a ser criado ou atualizado.

  Retorno:
    Nenhum.
  """

  # Abrir o arquivo CSV no modo de escrita.
  with open(nome_arquivo, 'w', newline='') as csvfile:

    # Criar um escritor CSV.
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Escrever as palavras no arquivo CSV.
    for palavra in palavras:
      csvwriter.writerow([palavra])


# Exemplo de uso
palavras = ["banana", "maçã", "laranja", "uva"]
nome_arquivo = "palavras.csv"

salvar_palavras_csv(palavras, nome_arquivo)

print(f"As palavras foram salvas no arquivo {nome_arquivo}")

"""
