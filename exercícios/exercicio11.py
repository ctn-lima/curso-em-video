#Faça um programa que leia a largura e a altura de uma parede em metros, 
#calcule a sua área e a quantidade de tinta necesssária para pintá-la, 
#sabendo que cada litro de tinta pinta uma área de 2m².

alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = alt * lar
tinta = int(area / 2)

if area % 2 > 0:
    tinta += 1

print('Uma parede com {:.2f}m de altura e {:.2f}m de largura possui {:.2f}m² de área e precisará de {} baldes de tinta para pintá-la'.format(alt, lar, area, tinta))