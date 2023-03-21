lados = []
lado0 = float(input('Digite um lado do triângulo: '))
lado1 = float(input('Digite outro lado do triângulo: '))
lado2 = float(input('Digite outro: '))
lados = sorted([lado0, lado1, lado2])
if (lados[0] + lados[1]) < lados[2]:
    mensagem = ('Não é possivel criar triângulo com lados {}, {} e {}.'.format(lado0,lado1,lado2))
else:
    mensagem = ('Pode-se fazer triângulo com os lados {}, {} e {}.'.format(lados[0],lados[1],lados[2]))
print(mensagem)
