def squareDigitsSequence(a0):
    
    squared = 0
    squared2 = 0
    count = 2
    seq = [a0]
    
    for i in str(a0):
        squared += pow(int(i), 2)

    while squared not in seq:
        print(seq, str(squared))
        for i in str(squared):
            squared2 += pow(int(i), 2)
        seq.append(squared)
        count += 1
        if squared2 in seq:
            print(seq)
            return count
        else:
            squared = squared2
            squared2 = 0

    return count