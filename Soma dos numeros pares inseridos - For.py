print('=-'*17+'\nSOMA DOS PARES INSERIDOS\n'+'=-'*17)
tamanho = int(input('Quantos números deseja somar: '))
lista = []
numeros = []
for numeros in range(0,tamanho,1):
    numeros = int(input('Digite um número: '))
    lista += [numeros]
    a = 0
    for i in lista:
        if i % 2 == 0:
            a += i
print(f'A soma dos pares inseridos é {a}.')
