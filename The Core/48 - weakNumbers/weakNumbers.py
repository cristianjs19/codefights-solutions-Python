def weakNumbers(n):

    divisors = 0
    groupDivisors = []
    weaker = 0
    weakness = 0
    groupWeakness = []
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            b = i % j
            if b == 0:
                divisors += 1
        groupDivisors.append(divisors)
        for i in range(len(groupDivisors)):
            if divisors < groupDivisors[i]:
                weakness += 1
        groupWeakness.append(weakness)
        if weakness > weaker:
            weaker = weakness
        divisors = 0
        weakness = 0
            
    return [weaker, groupWeakness.count(weaker)]