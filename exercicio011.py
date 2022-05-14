# Faça um programa que leia a largura e a altura de uma parede em M. Calcule a sua área e a quantidade necessária de tinta para pinta-lá, sabendo que cada litro de tinta
# pinta uma área de 2m^2
L = float(input('Qual o tamanho do lado da sua parede em metros? '))
h = float(input('Qual a altura da sua parede em metros? '))
A = L*h
print('Para pintar a sua parede, necessitará de {} Litros de tinta.'.format(A/2))