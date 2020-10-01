# Smallest number evenly divisible by numbers from 1 to 20

```python
import math 

def divisible_from_1_to_n(n):  
    number = 1
    for i in range(1, n + 1):  
        number = int((number * i)/math.gcd(number, i))          
    return number  

n = int(input())
print (divisible_from_1_to_n(n))
```
INPUT

```txt
20
```

OUTPUT

```txt
232792560
```
