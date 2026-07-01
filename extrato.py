def mostrar_extrato(extrato):
    print("===== EXTRATO =====")

    if len(extrato) == 0:
        print("Nenhuma movimentacao")
    else:
        for item in extrato:
            print(item)
