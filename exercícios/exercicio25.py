# Crie um programa que leia o nome de uma pessoa e deiga se ela tem "SILVA" no nome

nome = input('Digite um nome: ').strip()

lista = nome.upper().split()

if 'SILVA' in lista:
    print('A pessoa {} possui Silva no nome!'.format(nome.title()))
else:
    print('A pessoa {} não possui Silva no nome:'.format(nome.title()))