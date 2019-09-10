def pagesNumberingWithInk(current, numberOfDigits):
    
    while numberOfDigits > 0:
        if numberOfDigits - (len(str(current))) >= 0:
            numberOfDigits -= (len(str(current)))
            current += 1
        else:
            return current - 1
        
    return current - 1
