print('__'*17+'\nFILTRAGEM DE DADOS\n'+'__'*17) 

sexo = str(input('Iforme o sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, informe o sexo: ')).strip().upper()[0]
      
if sexo == 'M':
        print('Sexo masculino registrado com sucesso!')
if sexo == 'F':
        print('Sexo feminino registrado com sucesso!')