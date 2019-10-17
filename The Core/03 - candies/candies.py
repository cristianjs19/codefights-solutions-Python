def candies(n, m):

    while m % n != 0:
        m -= 1

    return m