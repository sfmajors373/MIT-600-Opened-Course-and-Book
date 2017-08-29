#Pay off the credit card in a year with a fixed monthly payment


#Variables
month = 0
balance = 5000
annualInterestRate = (.180/12.0)
monthlyPayment = 10

#First month
while month == 0:
    print("start")
    balance = balance - monthlyPayment
    month += 1
    print(str(balance) + "," + str(month))
    while 0 < month <= 12:
        balance = balance + (annualInterestRate * balance)
        balance = balance - monthlyPayment
        month += 1
        print(str(balance) + "," + str(month))
        if month == 12:
            if balance ==0:
                print("Lowest Payment: " + str(monthlyPayment))
            else:
                print(str(balance) + "," + str(month))
                month = 0
                balance = 5000
                monthlyPayment += 10
