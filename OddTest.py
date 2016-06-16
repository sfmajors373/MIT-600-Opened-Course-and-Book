#Input
largestoddnumbersofar = 0
counter = 0
#Test/Counter
while counter < 10:
    x = int(input("Enter a number: "))
    if x%2 == 1:
        if x > largestoddnumbersofar:
            largestoddnumbersofar = x
    counter = counter + 1
    print(counter)
    #Output
    if counter == 10:
        print ("The largest odd number is " + str(largestoddnumbersofar))
