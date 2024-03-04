

def factorial(inp):
    if inp == 0:
        return 1
    else:
        return inp * factorial(inp-1)

print(factorial(5))