# between()

**between(m: int,n: int)** Returns list of primes within given range[m,n]

```python
from primality import primality

primality.between(10,19)
>> [11, 13, 17, 19]
primality.between(100000,100001)
>> []
primality.between(10,11)
>> [11]
```