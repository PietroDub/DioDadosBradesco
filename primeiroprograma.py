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

