print('\n\nMÉDIA FINAL!\n'+'=-'*20)

nota1 = float(input('Digite a primeira nota:')[0:3])
nota2 = float(input('Digite a segunda nota:')[0:3])
media = (nota1 + nota2)/2

if media < 5:
    mensagem = ('Com a média {:.2f} você está reprovado.'.format(media))

elif 7 > media > 5:
    mensagem = ('Com a média {:.2f} você está de recuperação.'.format(media))

elif media >= 7:
    mensagem = ('Com a média {:.2f} você está aprovado.'.format(media))
#print(nota1,nota2,sep=',')
print(mensagem)
 