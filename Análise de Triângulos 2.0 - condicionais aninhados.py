print('\n\nANÁLISE DE TRIÂNGULOS\n'+'=-'*15)

lado1 = float(input('Digite o lado 1:  '))
lado2 = float(input('Digite o lado 2:  '))
lado3 = float(input('Digite o lado 3:  '))

lados = sorted([lado1,lado2,lado3])

if (lados[0] + lados[1]) < lados[2]:
    mensagem = ('Os lados {} e {} juntos são menores que {}, portanto não é possível '
                'formar um triângulo.'.format(lados[0],lados[1],lados[2]))

elif lados[0] == lados[1] == lados[2]:
    mensagem = ('O triângulo de lados {} é equilátero.'.format(lados[0]))

elif lados[0] == lados[1] or lados[1] == lados[2]:
    mensagem = ('O triângulo de lados {}, {} e {} é isósceles.'.format(lados[0],lados[1],lados[2]))

elif lados[0] != lados[1] and lados[1] != lados[2]:
    mensagem = (f'O triângulo de lados {lados[0]}, {lados[1]} e {lados[2]} é escaleno.')

print(mensagem)
