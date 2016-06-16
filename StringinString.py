x = str(input("Enter first phrase: "))
y = str(input("Enter second phrase: "))

if x in y:
    print("The first phrase was in the second phrase")
elif y in x:
    print("The second phrase was in the first phrase")
else:
    print("Neither phrase is in the other")


