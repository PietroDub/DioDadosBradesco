print ("Hello World! Again...")
int()
print (1 + 10)
float()
print (1.5 + 3)
bool()
print (True)
str()
print ("String")

# dir(), nomes do escopo local, ou do parâmetro
# help(), sistema de ajuda , trazendo, módulo, função, class, método, do geral ou parâmetro

# Variáveis:
age = 23
name = "Robert"
print(f"Meu nome é {name} e eu tenho {age}")

age = 19
name = "Anna"
print(f"Meu nome é {name} e eu tenho {age}")

# Python não tem constantes, então use MAIUSCULAS para constantes

STATES = [
    'SP',
    'RJ',
    'BA',
]
 
AMOUNT = 20.1

#conversão
numero = 10.5
print (numero)
numero = int(numero)
print (numero)

#input do usuário
nome = input("Informe seu nome:")
idade = input("Informe seu idade:")
print(nome, end="... \n")
print( nome, idade, sep=':')

# Operadores 

print(1 + 2)
print(10 - 2)
print(20 / 2)
print(20 // 2)
print(1 * 2)
print(2 ** 2)

saldo = 400
saque = 200
limite = 1000

print(saldo != saque)
print(saldo == saque)
print(saldo > saque)
print(saldo >= saque)

saldo += 100
print(saldo)

saldo **= 2

# Operador de negação
not 1000 > 1500

# E (saldo e limite tem q ser maior que saque)
saldo >= saque and saque <= limite

# OU (apenas saldo tem que ser maior que saque)
saldo >= saque or saque <= limite


print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

#Operadores de indentidade (SE OCUPA O MSM ESPAÇO NA MEMÓRIA)

curso = "Curso py"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
curso is not nome_curso
saldo is limite

# Operadores de associação
frutas = ["limao", "Uva"]

print ("limao" in frutas)
print ("uva" in frutas)
print ("limao" not  in frutas)