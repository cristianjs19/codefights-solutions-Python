def circleOfNumbers(n, firstNumber):
    jump = n / 2
    res = firstNumber + jump
    
    if res <= n-1:
        return res
    else: return res - n