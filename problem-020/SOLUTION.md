# Factorial Digit Sum

```python
num = 100
prod = 1
for i in range(1, num+1):
    prod = prod * i

sum([int(x) for x in list(str(prod))])
```

OUTPUT

```txt
648
```