# Crie um programa que leia uma frase e mostre quantes vezes a letra A aparece, em qual posição ela aparece na primeira vez e em qual posição ela aprece na última vez

frase = input('Digite qualquer frase: ').strip()

print('A frase "{}" possui {} letras A.'.format(frase.capitalize(), frase.upper().count('A')))
print('A primeira ocorrência de aparição da letra A na frase está na posição {}.'.format(frase.upper().find('A')+1))
print('A última ocorrência de aparidão da dela A na frase está na posição {}.'.format(frase.upper().rfind('A')))