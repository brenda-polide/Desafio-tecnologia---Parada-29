import os

print("------------------")
print("Cadastre as informações do seu produto")
print("                            ")

c = int(input("Digite seu código:"))
n =input("Digite seu nome:")
q = int(input("Digite a quantidade do produto: "))
p = int(input("Digite o preço do produto:"))

total = q * p

print("------------------")
print("Você cadastrou os seguintes dados do seu produto:")
print("------------------")

print("código:",c)
print("nome:",n)
print("quantidade:",q)
print("preço:",p)
print("Valor Total da compra é: R$ {}".format(total))
print("------------------")

os.system("pause")