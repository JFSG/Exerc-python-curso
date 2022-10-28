import math
ca = float(input('Qual o comprimento do c a?'))
co = float(input('Qual o comprimento do c o?'))
ch = math.hypot(ca, co)
print('A Hipotenusa vai medir {:.2f}'.format(ch))