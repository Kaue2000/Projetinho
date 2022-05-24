sexo = 'mulher'
altura = 1.60

if sexo == 'homem':
    result = (72.7 * altura) - 58
    print(f'peso ideal de ', result)
elif sexo == 'mulher':
    result = (62.1 * altura) - 44.7
    print(f'peso ideal de ', result)
