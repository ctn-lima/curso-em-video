#Faça um algoritmo que leia o salário de um funcionário e mostre o seu novo salário com 15% de aumento

salario = float(input('Digite o valor do salário: '))
aumento = salario * 0.15

print('O seu salário base de R${:.2f} teve um aumento de R${:.2f} e agora é R${:.2f}.'.format(salario, aumento, salario + aumento))