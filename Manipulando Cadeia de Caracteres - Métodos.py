
frase = 'oi Victor, tudo bem?'
len(frase)  # comprimento da frase
frase.count('o')  # quantas vezes tem a legra o em frase
frase.count('o', 0, 13)  # a contagem vai do primeiro ao
# décimo segundo caracter da string.
frase.find('tudo')  # vai identificar pela posição da primeira
# letra de 'tudo'
frase.find('tesouro')  # retorna valor -1, não há essa string
'tesouro' in frase  # retorna true
frase.replace('oi', 'olá')  # substitui em frase 'oi' por 'olá'
frase.upper()  # torna maiúsculo
frase.lower()  # torna tudo maiúsculo
frase.capitalize()  # [0] fica maiúsculo e o resto todo minúsaculo
frase.title()  # as primeiras letras das palavras em maiúsculo
frase.strip()  # remove espaço vazios antes e depois das letras
frase.rstrip()  # método strip pela direita, no fim da string
frase.lstrip()  # método strup pela esquerda, so no início da string
frase.split()  # cada espaço vazio na cadeia de caracteres é removido
# criando uma lista com todas as palavras separadas.
print('-'.join(frase))  # pega as palavras splitadas e junta-as com '-'
