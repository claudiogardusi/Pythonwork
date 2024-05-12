import pandas as pd
import numpy as np

# Nomes dos corredores
corredores = [
    "Ayrton Senna",
    "Nigel Mansell",
    "Alain Prost",
    "Gerhard Berger",
    "Nelson Piquet",
    "Michele Alboreto"]

# Gerar tempos aleatórios para cada volta de cada corredor
tempos = np.random.uniform(low=30, high=60, size=(10, 6))

# Titulo para voltas
df= pd.DataFrame(columns= corredores, data=tempos, index= [
    "Volta 1",
    "Volta 2",
    "Volta 3",
    "Volta 4",
    "Volta 5",
    "Volta 6",
    "Volta 7",
    "Volta 8",
    "Volta 9",
    "Volta 10"])

# Para ver o DataFrame decomente a proxima linha
#print("\n", df)

#Calculando a média dos tempos por corredor
media_tempos = df.mean(axis=0).sort_values()

print("\nAs médias de tempo dos corredores foram:")
print(media_tempos,'\n')

print('O vencedor foi "',df.sum().idxmin(),'" com a menor média de tempo!\n')
