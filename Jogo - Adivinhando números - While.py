print('__'*17+'\nJOGO - ADVINHANDO NÚMERO\n'+'__'*17) 
from random import randint
n = randint(0,10)
a = int(input('Acabei de pensar em um número de 0 a 10.\n'
              'Será que consegue adivinhar?\nR:'))
palpite = 1
while a != n:
    palpite += 1
    if a < n:
        a = int(input('Mais... tente outra vez.\n'
                      'informe seu palpite:'))
    if a > n:
        a = int(input('Menos... tente outra vez.\n'
                      'informe seu palpite:'))
print(f'Acertou em {palpite} tentativas! O número era {a}.')

'''
acertou = false
palpites = 0
while not acertou:
    a = int(input('Informe seu palpite: '))
    palpites += 1
    if a == n:
        acertou = true
    else:
        if a < n:
        a = int(input('Mais... tente outra vez.\n'
                      'informe seu palpite:'))
        if a > n:
        a = int(input('Menos... tente outra vez.\n'
                      'informe seu palpite:'))
print(f'Acertou em {palpite} tentativas! O número era {a}.')

'''