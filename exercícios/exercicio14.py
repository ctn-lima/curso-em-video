#Escreva um programa que converta uma tempuratura digitando em graus Celsius e converta para graus Fahrenheit
celsius = int(input('Quantos graus em Celsius você quer converter: '))
fahren = (celsius * 9 / 5) + 32

print('A temperatura de {:.1f}°C equivale a {:.1f}°F!'.format(celsius, fahren))