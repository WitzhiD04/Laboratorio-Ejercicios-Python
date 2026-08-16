# Crear una lista

from importlib import _bootstrap_external
L = ["Michael Jackson", 10.1, 1982, "MJ", 1]
print(L)

print(L[3:5])

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
print(L)


L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
print(L )

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

del(A[0])
print('After change del:', A)

print('A,B,C,D'.split(','))

# copia, no es la misma referencia
B = A[:]
B

print("--------------------------- ACA COMIENZA EL EJERCICIO------------------------")

a_list = [1, "hello", [1,2,3], True]
print(a_list)

print(a_list[1])

print(a_list[1:4])

A = [1, 'a']
B = [2, 1, 'd']

C = A + B
print(C)