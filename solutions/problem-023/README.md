# Non-Abundant Numbers

```python
abun = []
for i in range(1, 28123):
    factors = []
    for k in range(1, i//2+1):
        if i % k == 0:
            factors.append(k)
    if (sum(factors) > i):
        #print(i, factors)
        abun.append(i)

combinations = []
for num1 in abun:
    for num2 in abun:
        if num1+num2 <= 28123:
            combinations.append(num1+num2)

ab_com = set(combinations)
sum(set(range(1, 28123+1)) - ab_com)
```

OUTPUT

```txt
4179871
```
