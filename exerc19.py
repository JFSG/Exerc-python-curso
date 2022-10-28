from random import choice
n1 = input('Digite um nome: ')
n2 = input('Digite outro nome: ')
n3 = input('Digite mais um nome: ')
n4 = input('Digite só mais um nome: ')
sorteador = choice((n1, n2, n3, n4))
print('Quem vai apagar o quadro vai ser {}'.format(sorteador))