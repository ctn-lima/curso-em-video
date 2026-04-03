# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO"

cidade = input("Digite o nome de uma cidade: ").strip()

if cidade.upper().split()[0] == 'SANTO':
    print('A cidade informada começa com SANTO!')
    print(cidade.title())
else:
    print('A cidade informada não começa com SANTO. :(')
    print(cidade.title())