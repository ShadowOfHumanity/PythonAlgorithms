# RULE: ALL VOWELS A R E ,G.
vowels = "AaOoIiUuEe"

def translateVowels(string: str):
    for i in vowels:
        string = string.replace(i, "g")
    return string

 

print(translateVowels(input("Please Input Your Language To Translate It In Darian: ")))