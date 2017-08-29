#Practicing the use of the Try-Except Block
import re

string = input("Enter string here: ")
digits = []

def sumDigits(string):
    """Assumes s is a string
        Returns the sum of the decimal digits in s
            For example, if s is in 'a2b3c' it returns 5"""
    #listofNumbers = re.findall('/d+',string)
    #print(str(listofNumbers))
    #SumofAllNumbers = sum(listofNumbers)
    #print("The sum of the numbers in the string is " + str(SumofAllNumbers))


list(string)
for s in string:
#        try:
        if s.isdigit():
            digits.append(float(s))
            #print(str(digits))
            sum(digits)
            #print("Sum of digits is " + str(sum(digits)))
        #except ValueError:
        #    print(str(ValueError))
print("Sum of digits is " + str(sum(digits)))
