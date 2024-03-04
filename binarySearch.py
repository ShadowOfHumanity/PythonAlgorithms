import math

findW = ['a', 'b' , 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
findNum = [0, 5, 6, 10, 20, 27, 30, 35, 36, 37, 38, 60]

def binarySearch(target: int, start, end):
    global findNum
    if (start > end): # if the start is bgger then end which shouldnt be possible then its not found
        return "Not found"
    
    middle = math.floor((start + end)/2) 

    if (target == findNum[middle]):
        return "yay found it at index: "+str(middle)
    if target > findNum[middle]:
        return binarySearch(target, middle+1, end)
    if target < findNum[middle]:
        return binarySearch(target, start, middle-1)
        


print(binarySearch(60, 0, findNum.__len__()-1))


