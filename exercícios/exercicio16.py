#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Exemplo: 
# Digite um número:6.127 
# O número 6.127 tem a parte inteira 6.

from math import trunc

num = float(input('Digite um número com casas decimais: '))

print('O número {} tem a parte inteira {}'.format(num, trunc(num)))