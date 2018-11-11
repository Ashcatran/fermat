# coding: utf8
#!/usr/bin/env python3

import math

#FactorFermat(N): // N doit être impair
#A ← arrondi(sqrt(N))
#Bsq ← A*A - N
#tant que Bsq n'est pas un carré:
#A ← A + 1
#Bsq ← A*A - N // ou de façon équivalente : Bsq ← Bsq + 2*A + 1
#fin tant que
#retourner A - sqrt(Bsq) // ou A + sqrt(Bsq)

def isSquare(number):
    if number < 0:
        return False
    sqrt = math.sqrt(number)
    floorSqrt = math.floor(math.sqrt(number))
    return True if sqrt == floorSqrt else False

def isOdd(number):
    return False if number % 2 == 0 else True

if __name__ == '__main__':

    number =8000009 * 97 #3000017 * 3999971 #1933 * 2347 #83*97
    if isOdd(number):
        #print(number,"is odd")
        a = math.floor(math.sqrt(number))
        #print(a)
        bsq = a*a - number
        #print(bsq)
        while not isSquare(bsq):
            a +=1
            bsq = a*a - number
        result = a - math.sqrt(bsq)
        print(number, "=", result, "*", number/result)

    else:
        print(number, "is not odd")

