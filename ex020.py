from random import shuffle
n1 = str (input('Escreva o primeiro nome: '))
n2 = str (input('Escreva o segundo nome: '))
n3 = str (input('Escreva o terceiro nome: '))
n4 = str (input('Escreva o quarto nome: '))
lista = [n1 , n2, n3, n4]
resultado = shuffle (lista)
print('a ordem de apresentação é: \n{}' .format(lista))
