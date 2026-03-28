#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

a = input("Digite algo:")
print(type(a))
print("O valor digitado é alphanumerico? {}".format(a.isalnum()))
print("O valor digitado é alpha? {}".format(a.isalpha()))
print("O valor digitado está em maiúsculo? {}".format(a.isupper()))
print("O valor digitado é numerico? {}".format(a.isnumeric()))