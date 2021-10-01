# Concealed Square

## Python Solution

```python
def match(n):
    s = str(n)
    return not all(int(s[x*2]) == x+1 for x in range(9))


n = 138902663    # sqrt(19293949596979899)
while match(n*n):
    n -= 2

print(n*10)
```

OUTPUT

```text
1389019170
```
