# Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm.
n = float(input('Escreva o valor em METROS para ver quanto vale em cm e mm: '))
ncm = n*100
nmm = n*1000
print('{} em cm fica {} e em mm fica {}'. format(n, ncm, nmm))
