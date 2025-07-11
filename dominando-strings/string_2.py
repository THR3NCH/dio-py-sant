nome = "Luan"
idade = 23
profissao = "Programador"
linguagem = "Python"

dados = {"nome": "Luan", "idade": 23}

print("Nome: %s, Idade: %d" % (nome, idade))

print("Nome: {}, Idade: {}" .format(nome, idade))

print("Nome: {1}, Idade: {0}" .format(idade, nome))

print("Nome: {nome}, Idade: {idade}" .format(nome=nome, idade=idade))
print("Nome: {name}, Idade: {age} {name} {name} {age}" .format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))