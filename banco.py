saldo = 1000


def ver_saldo():
    print(f"Seu SALDO ATUAL E R$ {saldo:.2f}")


def depositar(valor, extrato):
    global saldo

    if valor <= 0:
        print("O deposito deve ser maior que zero!")
        return

    saldo += valor
    extrato.append(f"+ R$ {valor:.2f}")
    print("Deposito realizado com sucesso")


def sacar(valor, extrato):
    global saldo

    if valor <= 0:
        print("O saque deve ser maior que zero!")
    elif valor > saldo:
        print("Saldo INSUFICIENTE!")
    else:
        saldo -= valor
        extrato.append(f"- R$ {valor:.2f}")
        print("Saque realizado com sucesso")
