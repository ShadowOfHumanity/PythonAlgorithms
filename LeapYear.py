#Write a Python program to check if a given year is a leap year or not.


def leapYear(year):
    if year%4==0:
        return str(year)+" is a leap year."
    else:
        return str(year)+ " is not a leap year."
    
print(leapYear(20))