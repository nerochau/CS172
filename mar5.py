def fac2(n):
    return itfac2(n,1)

def itfac2(n,a):
    if n == 1: return a
    return itfac2(n-1, n*a)

fac2(3)