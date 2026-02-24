texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()  # adiciona uma quebra de linha

# Exemplo utilizando a função built-in range
# ínicio, fim, passo
for numero in range(0, 51, 5):
    print(numero, end=" ")


# Estrutura While
numero2 = 0

while numero2 != 100:
    numero2 += 1
    print(numero2)

opcao = -1

while opcao != 0:
    opcao = int(input("Escolha entre as opções: [1] Sacar [2] Depositar [3] SAIR"))

    if opcao == 1:
        print("Sacando...")
        break #para o código
    elif opcao == 2:
        print("Exibindo extrato..")

else:
    "O else vai no fim do loop no python!"