#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
x = input('Digite alguma coisa: ')
print('O tipo primitivo de {} é {}' .format(x, type(x)))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('Está em maiúsculas?', x.isupper())
print('Está em minúsculas?', x.islower())
print('Está capitalizada?', x.istitle())