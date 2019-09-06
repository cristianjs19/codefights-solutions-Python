def isPower(n):
    
    powGroup = [1]
    
    for i in range(2, 21):
        for j in range(2, 9):
            pow = i ** j
            if pow <= 400:
                powGroup.append(pow)
                
    if n in powGroup:
        return True
    else:
        return False