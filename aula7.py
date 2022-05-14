# Sinal de = é atribuição, == é para igualdade
# Ordem de Precedencia (), ** , * / // % , + -
n1 =  int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, o produto vale {} e a divisão vale {:.2f}'.format(s, m, d))
# Se não quiser que pule linha, colocar (, end=' ') depois do format
# Se quiser a quebra no meio do print, colocar (\n)
print('Divisão itenria vale {}, e a potência vale {}'.format(di, e))
