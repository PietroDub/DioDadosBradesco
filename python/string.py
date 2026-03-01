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