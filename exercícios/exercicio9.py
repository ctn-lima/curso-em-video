#Faça um programa que leia um número inteiro e mostre na tela sua tabuada.

n = int(input('Digite um número: '))

i = 1
print('-=================-')
while i < 10:
    print(' | {:2} x {:2} = {:2}  |'.format(n, i, n * i))
    i += 1
print('-=================-')
