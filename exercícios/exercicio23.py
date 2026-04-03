# Faça um programa que leia um número entre 0 e 9999 e mostre na tela cada dos dígitos separados
# Exemplo: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar 1

#Manipulando string:
num = input('Digite um número de 0 a 9999: ') # solicitando dados sem definir tipo de variável (Padrão: string) 
num2 = int(num) # transformando a string em número inteiro. Apenas para uso no próximo exemplo sem precisar digitar um novo número

while len(num) < 4: # Condicional para executar comando enquanto o tamanho da string(len) for menor que 4, garantindo que o dado digitado tenha 4 dígitos
    num = '0' + num # Acescentando um dígito zero a esquerda, caso o número digitado tenha menos que 4 dígitos. Também seria possível utilizar num.zfill(4)

# Imprimindo na tela o resultado, declarando cada caracteres correspondente da string em suas respostas.
print('\nO número digitado foi {} e possui:\nUnidade(s):{}\nDezena(s): {}\nCentena(s): {}\nMilhar(es): {}\n'.format(num, num[3], num[2], num[1], num[0]))



# Fórmula matemática para o mesmo resultado

#unidade → % 10
#dezena → // 10 % 10
#centena → // 100 % 10
#milhar → // 1000 % 10
print('\nO número digitado foi {} e possui:\nUnidade(s):{}\nDezena(s): {}\nCentena(s): {}\nMilhar(es): {}\n'.format(num2, num2 % 10, num2 // 10 % 10, num2 // 100 % 10, num2 // 1000 % 10))