#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

din = float(input('Digite quanto você tem em dinheiro: R$'))

dolar = 3.27
print('Com R${:.2f} e a cotação do dolar em $3.27, você conseguiria comprar US${:.2f} dolares.'.format(din, din / dolar))