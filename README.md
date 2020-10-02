# Primality

![PyPI](https://img.shields.io/pypi/v/primality)
![PyPI - Downloads](https://img.shields.io/pypi/dm/primality)

**Primality** helps you easily find, test and work with prime numbers in Python.

```python
primality.isprime(516349073509121311)
>> True

primality.nthprime(9999)
>> 104729

primality.prange(10)
>> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
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

For usage documentation and examples, please check out our [wiki](/wiki) and [docs](docs).

## Theory

The current version uses the Miller primality test (1) with known strong pseudoprime bases (2) to provide deterministic testing for integers between 2 and 2^64 - 1. (3)

- (1) : Miller, G. (1976), "Riemann's Hypothesis and Tests for Primality", Journal of Computer and System Sciences.

- (2) : Zhang, Z and Tang, M. (2003), "Finding strong pseudoprimes to several bases. II", Mathematics of Computation. 

- (3) : McCraine, J. (1997), "Sequence A014233 (Smallest odd number for which Miller-Rabin primality test on bases <= n-th prime does not reveal compositeness)". The On-Line Encyclopedia of Integer Sequences, OEIS Foundation. 

## Contributing

Contributions are welcome. Please remember to read [CONTRIBUTING.md](CONTRIBUTING.md) if it's your first time interacting with this project.
