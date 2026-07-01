from menu import MENU
import banco
from extrato import mostrar_extrato


extrato = []


def mostrar_menu():
    print("===== BANCO =====")

    for item in MENU:
        print(item)

    print("=================")


mostrar_menu()

while True:
    try:
        acesso = int(input("O que deseja acessar? "))
    except ValueError:
        print("Digite uma opcao valida!")
        print("=================")
        continue

    print("=================")

    if acesso == 1:
        banco.ver_saldo()

    elif acesso == 2:
        try:
            valor = float(input("Valor do deposito: R$ "))
            banco.depositar(valor, extrato)
        except ValueError:
            print("Digite um valor valido!")

    elif acesso == 3:
        try:
            valor = float(input("Valor do saque: R$ "))
            banco.sacar(valor, extrato)
        except ValueError:
            print("Digite um valor valido!")

    elif acesso == 4:
        mostrar_extrato(extrato)

    elif acesso == 5:
        mostrar_menu()

    elif acesso == 6:
        print("Saindo do sistema...")
        break

    else:
        print("Opcao invalida!")
