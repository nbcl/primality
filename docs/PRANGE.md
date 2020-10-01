# prange()

**prange(n: int)** Returns a list with the form of [2, 3, ..., {n}th prime].

```python
from primality import primality

primality.prange(3)
>> [2, 3, 5]
primality.prange(10)
>> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```