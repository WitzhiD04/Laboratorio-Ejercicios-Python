#for year in dates:  
    #print(year)  


# Usar el bucle for para cambiar los elementos de la lista

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])

print("--------------------------- ACA COMIENZA EL EJERCICIO------------------------")

for i in range(-5,6):
    print(i)


Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for genre in Genres:
    print(genre)

squares=['red', 'yellow', 'green', 'purple', 'blue']

print("\n")
for square in squares:
    print(square)

print("\n")

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

ratingActual = 7
i = 0
while ratingActual > 6:
    ratingActual = PlayListRatings[i]
    print(ratingActual)
    i=i+1

squares = ['orange', 'orange', 'purple', 'blue', 'orange']
new_squares = []
j = 0
print("\n")
while squares[j] == "orange":
    new_squares.append(squares[j])
    j=j+1
print(new_squares)
