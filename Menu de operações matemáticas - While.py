print('__'*17+'\nMENU DE OPERAÇÕES MATEMÁTICAS\n'+'__'*17) 

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0
while op != 5:
    op = int(input('[ 1 ] somar\n'
                   '[ 2 ] multiplicar\n'
                   '[ 3 ] maior\n'
                   '[ 4 ] novos números\n'
                   '[ 5 ] sair do programa\n'
                   'Insira a opção: '))
    if op == 1:
        print(f'{n1+n2}')
    if op == 2:
        print(f'{n1*n2}')
    if op == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2} o maior é {n1}.')
        elif n2 > n1:
            print(f'Entre {n1} e {n2} o maior é {n2}.')
    if op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida!')

print('Você finalizou o programa!')