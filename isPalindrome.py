
punctuation = "!,.:\"\\@#$%^&*()-=+[]{/}?><~`"
def isPalindrone(string : str):
    origString = string
    for char in punctuation:
        string = string.replace(char, "")
        #print(string)
    if (string[::-1].lower() == string.lower()):
        return origString+ " is a palindrome"
    else:
        return origString+ " is not a palndrome"
    
# WILL IGNORE PUNCTUATION AND CAPITAL LETTERS.
    
print(isPalindrone("NOoN.!"))
print(isPalindrone("o.!,K"))
print(isPalindrone("G.O!,d"))
print(isPalindrone("YAAAAAY!!!"))