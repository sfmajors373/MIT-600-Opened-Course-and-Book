#input
EnteredNumber = int(input("Enter number: "))
power = 2
root = 0

#Test and variables
while root**power != EnteredNumber:
    if root**power < EnteredNumber:
        root = root + 1
    if root**power > EnteredNumber:
        if power < 6:
            power = power + 1
        if power == 6:
            print("No such pair of numbers exist")
            break
    print("r+p " + str(root**power) + " : " + str(EnteredNumber))

#Output
if root**power == EnteredNumber:
    print("The root of " + str(EnteredNumber) + " is " + str(root) + " and the power is " + str(power) +".")
