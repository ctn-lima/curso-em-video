# Crie um programa que leia o nome de um pessoa e mostre
# O nome com todas as letras maiúsculas
# O nome com todas minúsculas
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = input('\nDigite o seu nome: ')
nome = nome.strip()

print('\nO nome em letras maiúsculas fica: {}'.format(nome.upper()))
print('\nO nome em letras minúsculass fica: {}'.format(nome.lower()))
print("\nO nome completo, possui {} letras.".format (len(''.join(nome.split()))))
print('\nO primeiro nome é {} e possui {} letras.\n'.format(nome.split()[0], (len(nome.split()[0]))))