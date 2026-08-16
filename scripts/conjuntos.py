set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(set1)


# Convertir una lista en un conjunto

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", \
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
print(album_set)

# Convertir una lista en un conjunto

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", \
                    "progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)


A = set(["Thriller", "Back in Black", "AC/DC"])
A.add("NSYNC") #remove para quitar
print(A)

print("AC/DC" in A)

intersection = set1 & music_genres
print(intersection)
print(set1.difference(music_genres))

print(set(set1).issuperset(music_genres))


print("--------------------------- ACA COMIENZA EL EJERCICIO------------------------")

genres = set(['rap','house','electronic music', 'rap'])
print(genres)

A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])

print(sum(A) == sum(B)) #Falso ya que el set quita números repetidos, lo que hace que cambia la suma al quitar un 2 

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

album_set3 = album_set1 | album_set2
print(album_set3)

print(album_set1.issubset(album_set3))