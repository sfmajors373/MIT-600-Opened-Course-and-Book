s = (input("Enter string: "))
count = 0
char = 0



def BobFinder(s):
    "Find bobs, Assumes string input, returns number of bobs in string"
    while char < len(s):
        if s[char] == "b":
            if s[char + 1] == "o":
                if s[char + 2] == "b":
                    count += 1
    print("The number of "bob" in string is " + str(counter))




testArray[aaazzz, aaabzzz, aaabozzz, aaabo, aaabobzz, aaabobozz, aaabobobzz]
testAnswers[0, 0, 0, 0, 1, 1, 2] 

#test thought process
#1 - for string in array, go through the while loop
#2 - append each answer from testArray into empty array
#3 - compare the testAnswers to experimentalAnswers array
#4 - print array locations that do not match

experimentalAnswers = []

def TestFunction(testArray):
    "Purpose is to test functionality and accuracy of original program"
    for thing in testArray:
        s = thing
        BobFinder(s)
        experimentalAnswers.append[counter]
    experimentalAnswers == testAnswers
