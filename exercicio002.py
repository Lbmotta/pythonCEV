#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas
nome = input('Digite seu nome:')
#meu jeito
print('Olá', nome, 'seja bem vindo(a)!')
#jeito "certo"
print('Olá {}, seja bem vindo(a)!'.format(nome))