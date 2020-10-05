import random
from primality import miller


def nthprime(nth: int):
    """Returns the nth prime, starting from n = 0, returning 2.

    Arguments:
        {nth} integer -- The {nth} position of the prime

    Raises:
        TypeError -- Wrong type for {nth} parameter, must be integer.
        ValueError -- Wrong value for {nth} integer, must be positive or zero.

    Returns:
        integer -- The {nth} prime.
    """

    if not isinstance(nth, int):
        raise TypeError("nthprime() takes (1) int type parameter. Given: "
    + str(type(nth)) + '.')
    if nth < 0:
        raise ValueError("nthprime() int parameter must be positive or zero.")
    if nth == 0 or nth == 1:
        return nth + 2
    prime_count = 1
    number = 5
    while True:
        is_prime = miller.miller(number)
        if is_prime:
            prime_count += 1
            if prime_count == nth:
                return number
        number += 2


def prange(n: int):
    """Returns a list in the form of [2, 3, ..., nth prime].

    Arguments:
        {n} integer -- The length of the list.

    Raises:
        TypeError -- Wrong type for {n} parameter, must be integer.
        ValueError -- Wrong value for {n} integer, must be positive or zero.

    Returns:
        List[integer] -- A list of continuous {n} primes, starting from 2.
    """

    if not isinstance(n, int):
        raise TypeError("prange() takes (1) int type parameter. Given: "
    + str(type(n)) + '.')
    if n < 0:
        raise ValueError("prange() int parameter must be positive or zero.")
    lists = [[], [2], [2,3]]
    if n in (0, 1, 2):
        return lists[n]
    primelist = [2,3]
    number = 5
    while True:
        is_prime = miller.miller(number)
        if is_prime:
            primelist.append(number)
            if len(primelist) == n:
                return primelist
        number += 2


def isprime(p: int):
    """True if p is prime.

    Arguments:
        {p} integer -- Integer number.

    Raises:
        TypeError -- Wrong type for {p} parameter, must be integer.

    Returns:
        True -- If {p} is prime.
        False -- If {p} is not prime.
    """

    if not isinstance(p, int):
        raise TypeError("isprime() takes (1) int type parameter. Given: "
    + str(type(p)) + '.')
    if p in (2,3):
        return True
    if p < 3:
        return False
    return miller.miller(p)


def between(m: int, n: int):
    """ Returns list of primes within given range[m,n]

    Arguments:
        {m} integer -- The starting index of Range
        {n} integer -- The Ending index of Range
    Raises:
        TypeError -- Wrong type for {m],{n} parameters, must be integer.
        ValueError -- Wrong value for {m},{n} integers, must be positive or zero.

    Returns:
        List[integer] --list of primes within given range[m,n].
    """
    if not isinstance(m, int):
        raise TypeError("between() expect parameter m to be int. Given: "
                        + str(type(m)) + '.')
    if not isinstance(n, int):
        raise TypeError("between() expect parameter n to be int. Given: "
                        + str(type(n)) + '.')
    primes = []
    if m > n:
        return primes
    if m <= 2 <= n:
        primes.append(2)
    number = m+1 if m % 2 == 0 else m
    if number < 0:
        number = 3
    while number <= n:
        if isprime(number):
            primes.append(number)
        number += 2
    return primes


def nextprime(n: int):
    """Returns the next prime number greater than n.

    Arguments:
        {n} integer -- Integer number

    Raises:
        TypeError -- Wrong type for {n} parameter, must be integer.

    Returns:
        integer -- The next prime number greater than n.
    """
    if not isinstance(n, int):
        raise TypeError("nextprime() expect parameter n to be int. Given: " +
                        str(type(n)) + '.')
    if n < 2:
        return 2
    number = n + 1 if n % 2 == 0 else n + 2
    while True:
        if isprime(number):
            return number
        number += 2


def prevprime(n: int):
    """Returns the previous prime number smaller than n.
    please notice: n must be larger than 2.

    Arguments:
        {n} integer -- Integer number

    Raises:
        TypeError -- Wrong type for {n} parameter, must be integer.
        ValueError -- Wrong value for {n} parameter, must be larger than 2.

    Returns:
        integer -- The previous prime number smaller than n.
    """
    if not isinstance(n, int):
        raise TypeError("prevprime() expect parameter n to be int. Given: " +
                        str(type(n)) + '.')
    if n < 3:
        raise ValueError("prevprime() expect parameter n to be larger than 2. "
                         "Given: " + str(n) + '.')
    if n == 3:
        return 2
    number = n - 1 if n % 2 == 0 else n - 2
    while True:
        if isprime(number):
            return number
        number -= 2

