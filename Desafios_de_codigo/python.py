valorSalario = input("Valor do salário Bruto")
valorBenefícios = input("Valor dos benefícios")

def CalcularImposto(valorSalario):
    aliquota = 0
    if valorSalario >= 0 and valorSalario <= 1100 :
        aliquota = 0.05
    elif valorSalario > 1100 and valorSalario <= 2500:
        aliquota = 0.10
    else:
        aliquota = 0.15
    return aliquota * valorSalario

valorImposto = CalcularImposto(valorSalario)

valortotal = valorImposto + valorBenefícios
print(valortotal)
