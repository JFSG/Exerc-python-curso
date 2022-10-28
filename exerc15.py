d = int(input('Quantos dias? '))
km = float(input('Quantos km rodados? '))
r = (km * 0.15) + (d * 60)
print('Você deverá pagar R${:.2f}'.format(r))