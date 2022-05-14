# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Escreva a nota do primeiro bimestre: '))
n2 = float(input('Escreva a nota do segundo bimestre: '))
m = (n1 + n2)/2
print('A nota do primeiro Bim. é {}, do segundo é {} e a média do aluno foi {}'.format(n1, n2, m))