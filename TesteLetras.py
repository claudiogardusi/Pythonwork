def trocar_por_numeros(string):
    vogais = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 't': '7'}
    nova_string = ''
    for letra in string:
        if letra.lower() in vogais:
            nova_string += vogais[letra.lower()]
        else:
            nova_string += letra
    return nova_string

texto= input('Digite o texto -->')
trocar_por_numeros(texto)