def lateRide(n):

    m = n % 60
    h = n // 60
    
    return h%10 + h//10 + m%10 + m//10