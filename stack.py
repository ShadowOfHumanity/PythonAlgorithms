myStack = []

def push(value):
    myStack.append(value)
    print(str(myStack[len(myStack)-1])+" is pushed in.")


def pop():
    print(str(myStack[len(myStack)-1])+" is popped out.")
    myStack.pop()

def peek():
    return myStack[len(myStack)-1]

def getSize():
    return len(myStack)

def showStack():
    return myStack

print(showStack)
print(push("Lol"))
print(push(5))
print(push(True))
print(push("8086x64"))
print(push((1, 2, 3)))
print(peek())
print(getSize())
print(pop())
print(pop())
print(showStack())