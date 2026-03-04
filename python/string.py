curso = "pYtHoN"

print(curso.upper())

print(curso.lower())

print(curso.title())

# Cortando palavras (trim)

print(curso.strip())

print(curso.center(10, "#"))

print(".".join(curso))


nome = "Pietro"
idade = 18
profissao = "Várias"
linguagem = "Python"

#interpolação 
print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {nome} Idade: {idade}".format(nome=nome,idade=idade))
print(f"Nome: {nome} Idade:{idade}")


texto = "Pietro Ama Fritas"

print(texto[0]) #primeiro char
print(texto[:9]) #acaba no char 9
print(texto[10:]) #comeca no char 10
print(texto[5:10]) #entre 5 e 10
print(texto[5:8:3]) 
print(texto[:])
print(texto[::-1]) #inverte


#strings triplas