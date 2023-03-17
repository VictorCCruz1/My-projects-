import time
date = time.gmtime()
month = date[1]
if month == 1:
    month = 'janeiro'
elif month == 2:
    month = 'fevereiro'
elif month == 3:
    month = 'março'
elif month == 4:
    month = 'abril'
elif month == 5:
    month = 'maio'
elif month == 6:
    month = 'junho'
elif month == 7:
    month = 'julho'
elif month == 8:
    month = 'agosto'
elif month == 9:
    month = 'setembro'
elif month == 10:
    month = 'outrubro'
elif month == 11:
    month = 'novembro'
elif month == 12:
    month = 'dezembro'
print('Dia {} de {} de {}.'.format(date[2], month, date[0]))
