# Quadratic Primes

```python
import math


def is_prime(num):
    prime = True
    if num < 2:
        return False
    if num == 2:
        return True
    for factor in range(3, int(math.sqrt(num)), 2):
        if num % factor == 0:
            prime = False
    return prime


def test_equation(a, b):
    n = 0
    while True:
        test = n**2 + a * n + b
        if is_prime(test):
            n += 1
        else:
            break
    return n


best = 0
besta = 0
bestb = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        c = test_equation(a, b)
        if c > best:
            best, besta, bestb = c, a, b

print(besta * bestb)
```

OUTPUT

```txt
-59231
```