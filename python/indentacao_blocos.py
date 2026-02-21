def sacar(valor):
    saldo = 400

    if saldo >= valor:
        saldo -= valor
        print("valor sacado!")
        print(f"saldo = {saldo}")

    else:
        print("Saldo muito baixo!")

    print("Obrigado por ser nosso cliente!")


sacar(100)