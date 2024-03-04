import math
#Write a Python program to generate a list of prime numbers within a specified range.

def genPrime(start:int, inpRangeEnd: int):
    primeNumbers = []
    for index in range(start, inpRangeEnd):
        lBool = isPrime(index)
        if lBool:
            primeNumbers.append(index)
    return primeNumbers

def isPrime(num: int):
    if num <= 1:
        return False
    for i in range(2, math.floor(math.sqrt(num))+1):
        if (num)%(i) == 0: ## all nums are divisible by 0, or 1, hence +2 is needed
            return False
    return True

def printList(tList: list):
    for num in tList:
        print(num)

#primeLists = genPrime(2, 10) #Note min is 2
printList(genPrime(2, 20))
