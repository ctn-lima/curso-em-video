#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenuisa

from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

h1 = hypot(co, ca)

print('Se o comprimento do cateto oposto é {:.2f} e o comprimento do cateto adjacente  {:.2f}, a hipotenusa vai medir {:.2f}'.format(co, ca, h1))