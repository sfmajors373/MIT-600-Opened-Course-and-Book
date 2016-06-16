s = (input("Enter string: "))
vowels =["a", "e", "i", "o", "u"]
count = 0

for char in s:
    if char in vowels:
        count +=1
print("The number of vowels in the string is " + str(count))

