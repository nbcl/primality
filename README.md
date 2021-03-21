# Primality

![PyPI](https://img.shields.io/pypi/v/primality)
![PyPI - Downloads](https://img.shields.io/pypi/dm/primality)

**Primality** helps you easily find, test and work with prime numbers in Python.

```python
primality.is_prime(516349073509121311)
>> True

primality.nth_prime(9999)
>> 104729

primality.prange(10)
>> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

primality.between(10,19)
>> [11, 13, 17, 19]

primality.next_prime(3)
>> 5

primality.prev_prime(1000)
>> 997

primality.rand_prime(10, 50, RandomStrategy.RANDOM_LIB)
>> 17

```

## Installation

Use the package manager [pip](https://pypi.org/) to install Primality.

```bash
pip install primality
```

## Implementation

Primality officially supports Python 3.8+.

```python
from primality import primality
```

## Documentation

For usage documentation and examples, please check out our [wiki](https://github.com/nbcl/primality/wiki) and [docs](docs).

## Theory

The current version uses the Miller primality test<sup>(1)</sup> with known strong pseudoprime bases<sup>(2)</sup> to provide deterministic testing for integers between 2 and 2<sup>64</sup> - 1<sup>(3)</sup>. For more details, please read [THEORY.md](theory/THEORY.md)

1. Miller, G. (1976), "Riemann's Hypothesis and Tests for Primality", Journal of Computer and System Sciences.

1. Zhang, Z and Tang, M. (2003), "Finding strong pseudoprimes to several bases. II", Mathematics of Computation. 

1. McCraine, J. (1997), "Sequence A014233 (Smallest odd number for which Miller-Rabin primality test on bases <= n-th prime does not reveal compositeness)". The On-Line Encyclopedia of Integer Sequences, OEIS Foundation.

## Contributing

Contributions are welcome. Please remember to read [CONTRIBUTING.md](CONTRIBUTING.md) if it's your first time interacting with this project.
