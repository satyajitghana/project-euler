# Multiples of 3 and 5

```python
def solution(k):
	"""Sum all multiples of 3 or 5 below k."""
	sum = 0
	for n in range(k):
		if n % 3 == 0 or n % 5 == 0:
			sum += n 
	return sum 

solution(1000) == 233168
```

OUTPUT

```shell
233168
```