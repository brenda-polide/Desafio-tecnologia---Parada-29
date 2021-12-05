import os

print("------------------")
print("Preencha as informações pedidas para o cadastro")
print("                            ")

nome = input("Digite seu nome:")
idade = input("Digite sua idade:")
telefone = input("Digite seu telefone:")
email = input("Digite seu email:")

print("------------------")
print("Você cadastrou os seguintes dados:")
print("------------------")

print("nome:",nome)
print("idade:",idade)
print("telefone:",telefone)
print("email:",email)
print("------------------")

os.system("pause")