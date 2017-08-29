# An iterative loop that calculates the value of a base to an exponent by iterative multiplication

base = float(input(str("Enter base: ")))

exp = int(input(str("Enter exponent: ")))

def iterPower(base, exp):
    """
    
    base: int or float
    exp: int >= 0
    return: int or float, base^exp
    
    """

    counter = 2
    result = 0
    if exp == 0:
        print(str("Answer is ") + str("1"))
    elif exp == 1:
        print(str("Answer is ") + str(base))
    elif exp > 1:
        while 2>= counter < exp:
            result = base * base
            counter += 1
        print(str("Answer is ") + str(result))


iterPower(base, exp)
            
