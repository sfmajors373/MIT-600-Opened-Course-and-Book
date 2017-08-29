#Using Bisection Search to calculate the lowest monthly payment that will pay off a $5,000 balance on a credit card with an 18% annual interest rate

#Basics

LowerBound = 5000/12 #lowest possible, balance divided by 12 months

UpperBound = 5000 #the balance with lots of interest divided by the 12 months


def midpointCalc(UpperBound, LowerBound):
    temporary =  ((UpperBound + LowerBound)/2)
    print(str("Midpoint is ") + str(temporary))
    return temporary

Midpoint = midpointCalc(UpperBound, LowerBound) 



payment = LowerBound 

annualInterest = (.180/12.0)

Balance =5000 

month = 0

def isLoanPaidinYear(month, LowerBound, UpperBound, Midpoint, Balance, annualInterest, payment):
    while 0 <= month < 12:

        if month == 0:
            print(str("start"))
            balance = Balance - payment
            month += 1
            print(str(balance) + "," +  str(month))
        else:
            balance = balance + (annualInterest * balance)
            balance = balance - payment
            month += 1
            print(str(balance) + "," + str(month))
        if month == 12:
            if balance == 0:
                print ("The lowest monthly payment is" + str(LowerBound))
                break
            elif balance > 0:
                LowerBound = Midpoint
                Midpoint = midpointCalc(UpperBound, LowerBound)
                month = 0
                print(str("not paid off"))
                continue
            elif balance < 0:
                UpperBound = Midpoint
                Midpoint = midpointCalc(UpperBound, LowerBound)
                month = 0
                print(str("over paid off"))
                continue


isLoanPaidinYear(month, LowerBound, UpperBound, Midpoint, Balance, annualInterest, payment)

