print('__'*17+'\nFATORIAL MANUAL\n'+'__'*17) 

n = int(input('Digite o número para descobrir seu fatorial: '))
f = n
print(f'Calculando fatorial de {n}, temos {n}! = {n} x ', end = '')
while n != 1:
    n = n - 1
    f = f * n
    print(f'{n}', end = '')
    print(' x ' if n > 1 else ' = ', end ='')
print(f'{f}')
