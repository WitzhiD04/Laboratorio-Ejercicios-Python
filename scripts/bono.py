def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)


print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,5))

print("\n")

#Galletas

def animal_crackers(text):
    letra1 = text[0]
    text2 = text.split()
    letra2 = text2[1][0]

    if letra1 == letra2:
        return True
    else:
        return False

print(animal_crackers('Ciudad Calor'))
print(animal_crackers('Lugar Frio'))

#DADOS
print("\n")

def makes_twenty(n1,n2):
    if n1 == 20 or n2 == 20:
        return True
    elif (n1+n2) == 20:
        return True
    else:
        return False

print(makes_twenty(20,10))
print(makes_twenty(2,3))
print(makes_twenty(12,8))

#mayusculas

print("\n")

def old_macdonald(name):
    new1 = name.capitalize()

    separate = new1[3:len(new1)]
    cap = separate.capitalize()

    final = new1.replace(new1[3:len(new1)], cap)

    return final

print(old_macdonald('macdonald'))

#reversa
print("\n")

def master_yoda(text):
    lista = text.split()
    n = len(lista) -1
    yoda = ''

    for i in range(n,-1,-1):
        yoda +=lista[i]
        yoda += ' '
    return yoda

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

#un 3 seguido
print("\n")

def has_33(nums):

    for i in range(0, len(nums) - 1):
        if nums[i] == 3 & nums[i] == nums[i+1]:
            return True

    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#Replicador
print("\n")

def paper_doll(text):
    resultado = ""
    for letra in text:
        resultado += letra * 3
    return resultado

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

#BlackJack
print("\n")

def blackjack(a,b,c):
    suma = 22
    if a+b+c <= 21:
        return a+b+c
    elif a+b+c > 21 & a == 11 or b == 11 or c == 11:
        suma = a+b+c-10
    
    if suma >= 21:
        return 'Bust!'
    else:
        return suma


print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
