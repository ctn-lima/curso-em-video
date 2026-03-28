#Faça um programa que leia um âmngulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math 

ang = float(input('Digite um ângulo: '))

print('Para o ângulo {}, temos os valores {:.2f} Seno, {:.2f} Cosseno e {:.2f} Tangente'.format(ang, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))