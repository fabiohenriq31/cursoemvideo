import math
co = float (input('Comprimento do cateto oposto: '))
ca = float (input('Comprimento do cateto adjacente: '))
print('A hipotenusa vai medir {:.2f}' .format(math.hypot(co,ca)))