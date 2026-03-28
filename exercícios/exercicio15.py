#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Bem vindo! Insira os dados solicitados para realização calculo de aluguel de veículo.')
dia = int(input('Informe por quantos dias o carro foi alugado: '))
km = float(input('Informe quantos km rodados foi utilizado: '))

dia = dia * 60
km = km * 0.15

print('O valor da diária ficou em R${:.2f} e o custo de kilometragem em R${:.2f} totalizando R${:.2f} o valor do aluguel.'.format(dia, km, dia + km))