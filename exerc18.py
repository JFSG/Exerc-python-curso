from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(an))
print('O ângulo de {:.2f}° tem o SENO DE {:.2f}°'.format(an, s))
t = tan(radians(an))
print('O ângulo de {:.2f}° tem o tangente de {:.2f}°'.format(an, t))
c = cos(radians(an))
print('O ângulo {:.2f}° tem o cosseno de {:.2f}°'.format(an, c))