print('\n\nGERENCIADOR DE PAGAMENTOS\n'+'=-'*15)

preço = float(input(('Qual valor total da compra?  ')))

pagamento = int(input('\nDIGITE:\n\n'
                      '\n[ 1 ] Para pagamento em dinheiro'
                      '\n[ 2 ] 1x em crédito ou débito'
                      '\n[ 3 ] 2x parcelado no cartão'
                      '\n[ 4 ] 3x ou mais no cartão'
                      '\nR:'))
if pagamento == 1:
    mensagem = (f'Com desconto de pagamento em dinheiro o total fica R${preço*0.9:.2f}')

elif pagamento == 2:
    mensagem = (f'Com desconto de pagamento sem parcela o total fica R${preço*0.95:.2f}')

elif pagamento == 3:
    parcela = preço/2
    mensagem = (f'Parcelamento em 2x de R${parcela:.2f} não tem acréscimo, o total fica R${preço:.2f}')

elif pagamento == 4:
    parcela = int(input('Informe o número de parcelas:'))
    parcelas = (preço*1.2) / parcela
    mensagem = (f'Parcelamento em {parcela}x de R${parcelas:.2f} acrescentou juros,'
                f' o total fica R${preço*1.2:.2f}')

else:
    
    mensagem = ('Opção inválida')

mensagem = str(mensagem.replace('.',','))
print(f'{mensagem}.')