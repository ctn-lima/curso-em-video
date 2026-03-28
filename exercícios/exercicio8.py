#Faça um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros

mt = float(input('Digite uma quantidade em metros: '))
cm = mt * 100
mm = mt * 1000
print('Você informou {:.1f} metros, que equivalem a {:.1f}cm e {:.1f}mm'.format(mt, cm, mm))