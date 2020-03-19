def isMAC48Address(inputString):
    
    chPair = ""
    chValid = "1234567890ABCDEF-"
    dash = 0
    
    if len(inputString) != 17:
        return False
    
    for i in inputString:
        if i not in chValid:
            return False
        if i != "-":
            chPair += i
            if len(chPair) > 2:
                return False
        else:
            chPair = ""
            dash += 1
            if dash > 5:
                return False
    
    return True