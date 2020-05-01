def competitiveEating(t, width, precision):
    return '{:{align}{width}.{prec}f}'.format( t, align='^', width= width, prec=precision)