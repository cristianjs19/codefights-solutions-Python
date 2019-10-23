def phoneCall(min1, min2_10, min11, s):
    
    min = 0

    if s >= min1:
        s -= min1
        min = 1
    for i in range(9):
        if s >= min2_10:
            s -= min2_10
            min += 1
        if s < min2_10:
            return min
    while s >= min11:
        s -= min11
        min += 1

    return min