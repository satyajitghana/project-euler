# Reciprocal cycles

```python
num = 1
longest_cycle = 1

for n in range(3, 1000, 2):
    if n % 5 == 0:
        continue

    cycle_length = 1
    while (10 ** cycle_length) % n != 1:
        cycle_length += 1

    if cycle_length > longest_cycle:
        num, longest_cycle = n, cycle_length

print(num)
```

OUTPUT

```
983
```
