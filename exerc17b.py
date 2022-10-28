ca = float(input('qual a medida do CA? '))
co = float(input('qual a medida do CO? '))
h = (ca**2 + co**2) ** (1/2)
print('A Hipotenusa vale {:.2f}'.format(h))