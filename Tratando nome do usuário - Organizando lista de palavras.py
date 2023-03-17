name = str(input('Type your name: ')).strip()
first_name = (name.split()[0])
middle_name = (' '.join(name.split()[1:-1]))
last_name = (name.split()[-1])
print('First name: {}.'.format(first_name))
print('Middle name: {}.'.format(middle_name))
print('Last name: {}.'.format(last_name))
print('Hello, {} {}! '.format(first_name, last_name))

# incluir condicional para último nome com preposição
