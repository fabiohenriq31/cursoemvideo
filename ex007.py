n1 = float (input ('Digite a primeira nota: '))
n2 = float (input ('Digite a segunda nota: '))
m = float ((n1 + n2) / 2)
media = 6.0
print ('A média das notas é de: {}' .format(m))
if m < media:
    print('Você foi reprovado!')
else:
    print('Você foi aprovado!')
