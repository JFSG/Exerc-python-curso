from hashlib import shake_128


n1 = int(input('Digite um numero: '))
s1 = n1+1
s2 = n1-1
print ('O Antecessor do numero {} é {}, e seu sucessor é {}'.format(n1, s2, s1))