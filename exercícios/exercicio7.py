#Faça um programa que leia duas notas de um aline, calcule e mostre a sua média
aluno = str(input('Digite seu nome: '))
nota1 = float(input('Digite sua primeira note: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
print('{} a média das suas notas é: ({:.1f} + {:.1f}) / 2 = {:.1f}'.format(aluno, nota1, nota2, media))