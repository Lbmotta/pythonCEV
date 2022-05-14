#teoria
#ERRADA(não é adição)(concatenação)
n1 = input('Digite um número:')
n2 = input('Digite mais um número')
s1 = n1 + n2
print('A soma vale:', s1)
#JEITO CERTO PARA SOMAR
#INT 7 -4 0 9875
#FLOAT 4.5 0.076 -15.223 7.0
#BOOL TRUE FALSE
#STR 'OLÁ' '7.5' ''
n3 = int(input('Digite um número'))
n4 = int(input('Digite mais um número'))
s2 = n3 + n4
print('A soma vale:', s2)
print('A soma vale: {}'.format(s2))
#OUTRA FORMA DE FAZER
print('A soma entre {} + {} é {}' .format(n3, n4, s2))