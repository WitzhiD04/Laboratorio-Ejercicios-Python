tuple1=(1,2,3)
print(tuple1)

print(type(tuple1))


print(tuple1[0])
print(tuple1[1])
print(tuple1[2])


print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

print(tuple2[3:5])



Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)

RatingsSorted = sorted(Ratings)
print(RatingsSorted)

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

print("--------------------------- ACA COMIENZA EL EJERCICIO------------------------")

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock","R&B", "progressive rock", "disco") 

print(len(genres_tuple))

print(genres_tuple[3])

print(genres_tuple[3:6])

print(genres_tuple[0:2])

print(genres_tuple.index("disco"))

C_tuple=(-5, 1, -3)

C_tuple = sorted(C_tuple)
print(C_tuple)