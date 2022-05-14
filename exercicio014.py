# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
C = float(input('Escreva o valor em graus Celsius: '))
F = C * 1.8 + 32
print('A temperatura em Fahrenheit é: {:.2f} graus'.format(F))