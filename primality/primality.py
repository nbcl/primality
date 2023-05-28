import random
import secrets

from primality import miller
from primality.random_strategy import RandomStrategy


def nth_prime(nth: int):
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
        raise TypeError("nth_prime() takes (1) int type parameter. Given: "
                        + str(type(nth)) + '.')
    if nth < 0:
        raise ValueError("nth_prime() int parameter must be positive or zero.")
    if nth == 0 or nth == 1:
        return nth + 2
    prime_count = 1
    number = 5
    while True:
        is_prime_number = miller.miller(number)
        if is_prime_number:
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
    lists = [[], [2], [2, 3]]
    if n in (0, 1, 2):
        return lists[n]
    prime_list = [2, 3]
    number = 5
    while True:
        is_prime_number = miller.miller(number)
        if is_prime_number:
            prime_list.append(number)
            if len(prime_list) == n:
                return prime_list
        number += 2


def is_prime(p: int):
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
        raise TypeError("is_prime() takes (1) int type parameter. Given: "
                        + str(type(p)) + '.')
    if p in (2, 3):
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
    number = m + 1 if m % 2 == 0 else m
    if number < 0:
        number = 3
    while number <= n:
        if is_prime(number):
            primes.append(number)
        number += 2
    return primes


def next_prime(n: int):
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
        if is_prime(number):
            return number
        number += 2


def prev_prime(n: int):
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
        raise TypeError("prev_prime() expect parameter n to be int. Given: " +
                        str(type(n)) + '.')
    if n < 3:
        raise ValueError("prev_prime() expect parameter n to be larger than 2. "
                         "Given: " + str(n) + '.')
    if n == 3:
        return 2
    number = n - 1 if n % 2 == 0 else n - 2
    while True:
        if is_prime(number):
            return number
        number -= 2


def rand_prime(m: int, n: int, strategy: RandomStrategy = RandomStrategy.RANDOM_LIB):
    """
    Arguments:
        {m} integer -- The Starting index of Range
        {n} integer -- The Ending index of Range

    Returns:
        integer -- A random prime number between m and n.

    """
    if not isinstance(m, int):
        raise TypeError("rand_prime() expect parameter m to be int. Given: "
                        + str(type(m)) + '.')
    if not isinstance(n, int):
        raise TypeError("rand_prime() expect parameter n to be int. Given: "
                        + str(type(n)) + '.')

    found_primes = between(m, n)
    if len(found_primes) == 0:
        return -1

    if strategy is RandomStrategy.RANDOM_LIB:
        return random.choice(found_primes)
    elif strategy is RandomStrategy.SECRETS_CHOICE:
        return secrets.choice(found_primes)
    elif strategy is RandomStrategy.SECRETS_RANDOM:
        return secrets.SystemRandom().choice(found_primes)
    else:
        raise ValueError("Couldn't find the selected strategy")

def next_prime_after_operation(n : int, m : int, operation : str):
    """
    Arguments:
        {n} integer -- The Starting index of Range
        {m} integer -- The Ending index of Range
        {string} string -- The operation to be performed

    Returns:
        integer -- The next prime number after the sum of the operation
    """
    if not isinstance(n, int):
        raise TypeError("next_prime_after_sum() expect parameter n to be int. Given: "
                        + str(type(n)) + '.')
    if not isinstance(m, int):
        raise TypeError("next_prime_after_sum() expect parameter m to be int. Given: "
                        + str(type(m)) + '.')
    if not isinstance(operation, str):
        raise TypeError("next_prime_after_sum() expect parameter string to be string. Given: "
                        + str(type(operation)) + '.')
    if operation == "+":
        return next_prime(n + m)
    elif operation == "-":
        return next_prime(n - m)
    elif operation == "*":
        return next_prime(n * m)
    elif operation == "/":
        return next_prime(int(n / m))
    else:
        raise ValueError("Couldn't find the selected operation")


def prev_prime_before_operation(n : int, m : int, operation : str):
    """
    Arguments:
        {n} integer -- The Starting index of Range
        {m} integer -- The Ending index of Range
        {string} string -- The operation to be performed

    Returns:
        integer -- The previous prime number before the operation
    """
    if not isinstance(n, int):
        raise TypeError("prev_prime_before_op() expect parameter n to be int. Given: "
                        + str(type(n)) + '.')
    if not isinstance(m, int):
        raise TypeError("prev_prime_before_op() expect parameter m to be int. Given: "
                        + str(type(m)) + '.')
    if not isinstance(operation, str):
        raise TypeError("prev_prime_before_op() expect parameter string to be string. Given: "
                        + str(type(operation)) + '.')
    if operation == "+":
        return prev_prime(n + m)
    elif operation == "-":
        return prev_prime(n - m)
    elif operation == "*":
        return prev_prime(n * m)
    elif operation == "/":
        return prev_prime(int(n / m))
    else:
        raise ValueError("Couldn't find the selected operation")