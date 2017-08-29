#Newton-Raphson for square foot
#Find x such that x**2 - 24 is within epsilon of 0

epsilon = 0.01
counter  = 0
k = 24.0
guess = 2/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2)-k)/(2*guess))
    counter = counter + 1
print('Square root of ' + str(k) + ' is about ' + str(guess) + " and it took " + str(counter) + " tries to find it.")
