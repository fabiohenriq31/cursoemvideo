import math

x = float (input('Digite o ângulo que você deseja: '))
rad = math.radians(x)
print('O ângulo de {} tem o SENO de {:.2f}'.format(x, math.sin(rad)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(x, math.cos(rad)))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(x, math.tan(rad)))