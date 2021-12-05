import os

lado=int(input('Digite o lado do quadrado:'))

area = lado * lado

print('A área do quadrado é:', area)

altura = int(input('Digite a altura do triãngulo:'))
base = int(input('Digite a base do triãngulo:'))

area = (base * altura)/2

print('A área do triãngulo é:', area)

os.system("pause")