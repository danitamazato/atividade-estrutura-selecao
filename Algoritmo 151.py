peso = float(input('\n Digite o peso, em Kg: '))
altura = float(input('\n Digite a altura, em metros: '))
imc = peso / altura ** 2

if imc < 20:
    print ('\n Abaixo do peso.')
elif imc <= 25:
    print ('\n Normal.')
elif imc <= 30:
    print ('\n Excesso de peso.')
elif imc <= 35:
    print ('\n Obesidade.')
else:
    print ('\n Obesidade mórbida.')
print ('\n')