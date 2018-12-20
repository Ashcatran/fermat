# coding: utf8
#!/usr/bin/env python3

import math

import sys

#Pseudo Code from https://fr.wikipedia.org/wiki/M%C3%A9thode_de_factorisation_de_Fermat
#FactorFermat(N): // N doit être impair
#A ← arrondi(sqrt(N))
#Bsq ← A*A - N
#tant que Bsq n'est pas un carré:
#A ← A + 1
#Bsq ← A*A - N // ou de façon équivalente : Bsq ← Bsq + 2*A + 1
#fin tant que
#retourner A - sqrt(Bsq) // ou A + sqrt(Bsq)

def isSquare(number):
    """returns True if number is a sqare"""
    if number < 0:
        return False
    sqrt = math.sqrt(number)
    floorSqrt = math.floor(math.sqrt(number))
    return True if sqrt == floorSqrt else False

def isOdd(number):
    """returns True if number is Odd"""
    return False if number % 2 == 0 else True

def fermat(number):
    """Returns one of the factors of number"""
    if isOdd(number):
        a = math.floor(math.sqrt(number))
        bsq = a*a - number
        while not isSquare(bsq):
            a +=1
            bsq = a*a - number
        result = a - math.sqrt(bsq)
        return int(result)
    else:
        return -1

if __name__ == '__main__':
    #8000009 * 97 #3000017 * 3999971 #1933 * 2347 #83*97
    print(sys.version_info)
    if len(sys.argv) == 2:
        user_in = int(sys.argv[1])
    else:
        try:
            user_in = int(input("Please enter the number you wish to factorize: "))
        except ValueError:
            print("You must specify an integer")
            exit()
    
    number = int(user_in)
    result = fermat(number)
    if result == -1 :
        print(str(number) + " is not odd")
    elif result == 1:
        print(str(number) + " is prime !")
    else:    
        print(str(number) + " = " + str(result) + " * " + str(int(number/result)))
