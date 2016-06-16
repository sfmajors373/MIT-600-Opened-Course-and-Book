#Problem Set2.1


#Variables
month = 0
balance = 5000
annualInterestRate = (12.0/18.0)
monthlyPayment = balance*0.02
totalPaid = 0


#First month
while month = 0:
    print("Month: " + str(month) + \n + "Minimum Monthly Payment: " + str(round(monthlyPayment,2)) + \n + "Remaining Balance: " + str(balance))
    month += 1
    totalPaid = monthlyPayment
#Remaining months
while 0 < month <= 12:
    balance = balance + (annualInterestRate)(balance)
    balance = balance - monthlyPayment
    print("Month: " + str(month) + \n + "Minimum Monthly Paymenbt: " + str(round(monthlyPayment,2)) + \n + "Remaining Balance: " + str(round(balance,2)))
    month += 1
    totalPaid = totalPaid + montlypayment
#Final Print
while month = 12:
    print("Total Paid: " + str(round(totalPaid,2)) + \n + "Remaining Balance: " + str(round(balance,2)))
