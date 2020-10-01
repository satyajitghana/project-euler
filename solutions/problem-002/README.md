# Even Fibonacci numbers

```python
def solution():
	x = 1  # Represents the current Fibonacci number being processed
	y = 2  # Represents the next Fibonacci number in the sequence
	ans = 0
	while x <= 4000000:
		if x % 2 == 0:
			ans += x
		x, y = y, x + y
	return ans
```

OUTPUT

```shell
4613732
```