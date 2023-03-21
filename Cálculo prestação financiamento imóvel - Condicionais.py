imovel = float(input('Qual valor do imóvel?'))
salario = float(input('Qual valor do seu salário?'))
salario_disponivel = salario * 0.3
tempo = int(input('Em quantos anos vai pagar?'))
prestaçao = (imovel/(tempo*12))

if prestaçao >= salario_disponivel:
    mensagem = ('Impréstimo não disponível, seu limite é {:.2f} e a parcela ficou em {:.2f}.'.format(salario_disponivel,prestaçao))

elif prestaçao <= salario_disponivel:
    mensagem = ('A parcela será de {:.2f} para ser paga em {:.0f} anos.'.format(prestaçao,tempo))

print(mensagem)
