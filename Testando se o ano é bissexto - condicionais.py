ano = float(input('Qual ano será analizado? Digite 0 (zero) para saber o atual:'))
bissexto = ano%4
bissexto100 = ano%100
bissexto400 = ano%400
if  ano == 0 :
    from time import gmtime
    if (gmtime()[0]%4) == 0:
        print ('Seu ano é {:.0f} e ele é bissexto.'.format(gmtime()[0]))
    else:
        print ('Seu ano é {:.0f} e ele não é bissexto.'.format(gmtime()[0]))
elif (bissexto == 0 and bissexto100 != 0) or (bissexto400 == 0) :
    print('O ano {:.0f} é bissexto.'.format(ano))
else:
    print('O ano {:.0f} não é bissexto.'.format(ano))

#pode ser aprimodo para ano receber 'atual' e imprimir o resultado para ano==string false or true