# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do ssegundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')

alunos = [al1, al2, al3, al4]
shuffle(alunos)

print("A ordem de apresentação de trabalho será: {}".format(alunos))