def GCD(a, b):
    if  (a==b):
        return a 
    elif (a>=b):
        if b==0:
            return a
        r = a%b
        a = b
        b = r
        return GCD(a, b) 

print(GCD(10, 5))