conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque Realizado com Sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque Realizado com Sucesso com uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque Realizado com Sucesso!")
    else:
        print("Saldo Insuficiente!")
else:
    print("sistema não reconheceu seu tipo de conta, entre em contato com seu gerente!")