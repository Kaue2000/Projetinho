peso = 60
altura = 1.60
altura2 = altura * altura
imc = peso / altura2

if imc <= 18.5:
    print(imc, f'Abaixo do peso')
elif 18.6 <= imc <= 24.9:
    print(imc, f'Saudável')
elif 25 <= imc <= 29.9:
    print(imc, f'Peso em excesso')
elif 30 <= imc <= 39.9:
    print(imc, f'Obesidade')
else:
    print(imc, f'Obesidade Grave')
