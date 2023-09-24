import math

x = float(input('\n Digite o valor de x: '))

if x <= 1:
    y = 1
elif x <= 2:
    y = 2
elif x <= 3:
    y = x**2
else:
    y = x**3

print('\n Valor de f(x): ', y)
print ('\n')
