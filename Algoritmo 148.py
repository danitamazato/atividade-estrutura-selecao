op = int(input('\n Digite 1- Região Norte; 2- Região Nordeste; 3- Região Centro-Oeste; 4- Região Sul: '))
iv = int(input('\n Digite 1- Ida; 2- Ida e Volta: '))

if op == 1:
    if iv == 1:
        print('\n O valor da passagem de ida para R.Norte: R$500.00')
    else:
        print('\n O valor da passagem de ida-volta para R.Norte: R$950.00')
elif op == 2:
    if iv == 1:
        print ("\n O valor da passagem de ida-volta para R.Nordeste: R$350.00")
    else:
        print('\n O valor da passagem de ida-volta para R.Nordeste: R$650.00')
elif op == 3:
    if iv == 1:
        print('\n O valor da passagem de ida para R.C.Oeste: R$350.00')
    else:
        print ('\n O valor da passagem de ida-volta para R.C.Oeste: R$600.00')
elif op == 4:
    if iv == 1:
        print('\n O valor da passagem de ida para R.Sul: R$300.00')
    else:
     print('\n O valor da passagem de ida-volta para R.Sul: R$550.00')
else:
    print('\n Opção Inexistente')

print ('\n')