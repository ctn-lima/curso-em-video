#Faça um programa que leia um número inteiro e mostre seu dobro, seu triplo e raiz quadrada.
n = int(input('Digite um número:'))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O número digitado foi {}. \nSeu dobro é {}.\nSeu triplo é {}. \nSua raiz quadrada é {}'.format(n , dobro, triplo, raiz))