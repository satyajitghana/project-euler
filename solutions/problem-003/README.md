# Largest prime facror of 600851475143

```python
import math 

def prime_factors(n): 
    result = [0]
    while n % 2 == 0: 
        result.append[2]
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            result.append(i)
            n = n / i 
    if n > 2: 
        result.append(n)
    return result[-1]
            
n = int(input())
print(prime_factors(n))
```
INPUT

```txt
600851475143
```

OUTPUT

```txt
6857
```
