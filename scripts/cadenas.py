
Name = "Michael Jackson"
Name

# Imprime el último elemento de la cadena

print(Name[-1])

# Encuentra la longitud de la cadena

len("Michael Jackson")

Name[8:12]

print(Name[8:12])
print(Name[0:4])

print(Name[::2])

print(Name[0:5:2])

print(Name)


print(" Michael Jackson \t is the best" )
print(r" Michael Jackson \ is the best" )

A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)

A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
print(B)

print(Name.find('Jack'))

#### EJERCICIO #######
print("--------------------------- ACA COMIENZA EL EJERCICIO------------------------")

A = "1"
print(A)

B = "2"
print(B)

C = A + B
print(C)

D = "ABCDEFG"
print(D[0:3])

E = 'clocrkr1e1c1t'
print(E[::2])

print("\\")

F = "You are wrong"

F = F.upper()

print(F)

G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb \
Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go"

print(G.find('snow'))

G = G.replace("Mary", "Bob")

print(G)