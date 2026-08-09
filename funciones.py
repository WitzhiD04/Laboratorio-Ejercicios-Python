import random

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)
print(sum(album_ratings))

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

print("--------------------------- ACA COMIENZA EL EJERCICIO------------------------")

def div(a,b):
    print(a,"dividido", b)
    return a/b

print(div(random.randint(0,1000),random.randint(1,1000)))

print("\n")

def con(a, b):
    return(a + b) #si se puede para ambos cadenas y enteros ya que puede tanto sumar numero como concatenar cadenas

print(con(2,2))
print(con("a","b"))

#Tambien se puede con listas y tuplas, lo que hace simplemente es juntar ambas en una sola

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
tupla1 = (6,2,10,373)
tupla2 = (34,67,60,47)
print(con(lista1,lista2))
print(con(tupla1,tupla2))