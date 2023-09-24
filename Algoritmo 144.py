saldo_medio = float(input("\n Digite saldo médio (R$): "))

if saldo_medio < 501:
    credito = 0
elif saldo_medio <1001:
    credito = saldo_medio * 0.3
elif saldo_medio <3001:
    credito = saldo_medio * 0.4
else:
    credito = saldo_medio * 0.5

if credito != 0:
    print(f"\n Como seu saldo era de R${saldo_medio:.2f}, seu crédito será de R${credito:.2f}.")
else:
    print(f"\n Como seu saldo era de R$ {saldo_medio:.2f}, você não terá nenhum crédito.")
print("\n")