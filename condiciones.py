import random

print("ACDC" != "Michael Jackson")

print('BA' > 'AB')

# Ejemplo de condicion if

age = 19
age = 18

#La expresión que puede ser verdadera o falsa
if age > 18:
    
    #parte con sangría, esta es la expresión que será ejecutada si la condición es verdadera
    print("you can enter" )
else:
    print("go see Meat Loaf" )
#Las declaraciones después de la condición if serán ejecutadas independientemente de si la condición 
#es verdadera o falsa
print("move on")





print("--------------------------- ACA COMIENZA EL EJERCICIO------------------------")

disco = 8.5

if(disco > 8):
    print("This album is Amazing!")

disco = random.randint(0,10)

if(disco > 8):
    print("This album is Amazing!")
else:
    print("this album is ok")

disco2 = random.randint(1960,2000)
print("año del disco ", disco2)

if disco2 < 1980:
    print("El disco salió previo a 1980")
elif disco2 == 1991 or disco2 == 1993:
    print("El disco salió en 1991 o 1993")
    