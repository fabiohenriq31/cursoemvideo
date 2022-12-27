import random
a = input('Escreva um nome: ')
b = input('Escreva um nome: ')
c = input('Escreva um nome: ')
d = input('Escreva um nome: ')
lista = [a,b,c,d]
print('o nome escolhido foi: {}'.format(random.choices(lista)))