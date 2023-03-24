print('=-'*17+'\nDETECTOR DE PALÍNDROME\n'+'=-'*17)

frase = str(input('Digite a frase: ')).strip().upper()
palavra = ''.join(frase.split())
inverso = ''
for i in range (len(palavra) -1, -1, -1):
    inverso += palavra[i]
    if inverso == palavra:
        mensagem = (f'Temos um palíndrome, {inverso}!')
    else:
        mensagem = (f'Não temos um palíndrome, a palavra é {palavra} e o inverso é {inverso}!')

print(mensagem)

'''inverso= palvra[::-1]   funcionaria do mesmo jeito'''