def sacar(valor):
    saldo = 400

    if saldo >= valor:
        saldo -= valor
        print("valor sacado!")
        print(f"saldo = {saldo}")

    else:
        print("Saldo muito baixo!")

    print("Obrigado por ser nosso cliente!")


sacar(100 )

#elseif

opcao = int(input("Informe: [1] Sacar / [2] Depositar: "))

if opcao == 1:
    valor = float(input("Informe a quantida de saque:"))
elif opcao == 2:
    valor = float(input("Informe o valor do depósito:"))
else:
    exit("Opção inválida")

#if dentro de if
idade = int(input("Idade:"))
opcao = int(input("Informe: [1] Sacar / [2] Depositar: "))


if idade > 18:
    if opcao == 1:
        valor = float(input("Informe a quantida de saque:"))
    elif opcao == 2:
        valor = float(input("Informe o valor do depósito:"))
    else:
        exit("Opção inválida")
elif idade > 12 and idade < 18:
    print("Acesso a recursos limitados!")
else:
    print("Acesso Negado!")


# if ternário

status = "Garantido" if idade >= 18 else "Negado"
print(f"Status de entrada: {status}")