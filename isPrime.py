import math

#Write a Python program to check if a given number is prime or not.

def isPrime(num: int):
    if num <= 1:
        return "Not Prime"
    for i in range(2, math.floor(math.sqrt(num))+1):
        if (num)%(i) == 0: ## all nums are divisible by 0, or 1, hence +2 is needed
            return "Not Prime"
    return "Is Prime"

print(isPrime(5))
print(isPrime(7))  
print(isPrime(9))
print(isPrime(16))
print(isPrime(37))
print(isPrime(0))
print(isPrime(1))
print(isPrime(2))