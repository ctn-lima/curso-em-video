#Faça um algoritmo que leia o preço de um produto e mostre o seu preço com 5% de desconto.

preco = float(input('Digite o valor do produto: R$'))
desconto = preco * 0.05

print('O valor digitado foi R${:.2f} e produto sai por R${:.2f} com 5%_ de desconto. Uma economia de R${:.2f}'.format(preco, preco - desconto, desconto))