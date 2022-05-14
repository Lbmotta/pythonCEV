# Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
Km = float(input('Quantos Km foi percorrido? '))
Dias = int(input('Quantos dias foi alugado? '))
C1 = Km * 0.15
C2 = Dias * 60
T = C1 + C2
print('Você terá que pagar {:.2f} pelos Km percorridos + {} pelos dias do carro alugado. TOTAL = {}'.format(C1, C2, T))