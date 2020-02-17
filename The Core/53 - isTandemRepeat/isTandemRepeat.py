def isTandemRepeat(inputString):
    
    midLen = len(inputString) // 2
    firstHalf = inputString[0:midLen]
    secondHalf = inputString[midLen:]    
    
    if firstHalf == secondHalf:
        return True
    else:
        return False