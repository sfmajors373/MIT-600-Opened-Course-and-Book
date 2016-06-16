l = (input("Enter a list of integers: "))
evens = []

def findAnEven(l):
    """Assumes l is a list of integers
       Returns the first even number in l
       Raises ValueError if l does not contain an even number"""
    #l = int(l)
    l =  l.split(",")
    for char in l:
        char = int(char)
        try:
            if char%2 == 0:
                evens.append(char)
                #print(char)
        except:
            raise ValueError("no evens in list")
    print("Evens: " + str(evens))

findAnEven(l)

