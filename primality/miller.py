import random


def miller(p: int):
    """Miller primality test.

    Arguments:
        {p} integer -- The {p} number.

    Returns:
        True -- If {p} is prime.
        False -- If {p} is not prime.
    """        
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if p in bases:
        return True
    r, d = 0, p - 1
    while d % 2 == 0: 
        d, r = d // 2, r + 1
    for a in bases:
        x = pow(a, d, p)
        if x == p - 1 or x == 1: 
            continue
        for __ in range(r - 1):
            x = pow(x, 2, p)
            if x == p - 1: 
                break
        else: 
            return False
    return True
