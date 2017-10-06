
def rowswap(a, r1, r2):

    b  = a

    b[r1] = a[r2]
    b[r2] = a[r1]

    return b

def krow(a, k, r):

     a[r] = k * a[r]

     return a

def krowrep(a, r1, r2, k):

    a[r1] = a[r1] + k * a[r2]

    return a