print('__'*17+'\nANALISANDO DADOS DE PESSOAS\n'+'__'*17)

media = 0
mulheres = 0
nomev = ''
for i in range(1,5,1):
    print(f'---- {i}ª pessoa ----')
    nome = str(input('nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input("sexo [F/M]: "))
    media += idade

    if sexo in 'Ff':
        if idade < 20:
            mulheres += 1

    else: 
        nomev = nome
        velho = idade
        if idade > velho:
            nomev = nome
            velho = idade
media = media/4

print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho possui {velho} anos e se chama {nomev}.')
print(f'Ao todo são {mulheres} mulheres com menos de 20 anos.')