from random import shuffle
n1 = input('Digite um nome: ')
n2 = input('Digite outro nome: ')
n3 = input('Digite mais um nome: ')
n4 = input('Digite só mais um nome: ')
a = [n1, n2, n3, n4]
shuffle(a)
print('Os alunos são {}, {}, {} e {}, e a ordem de quem vai apresentar é {}'.format(n1, n2, n3, n4, a))

