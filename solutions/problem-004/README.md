# Largest Palindrome Product

```python
def is_palindrome(num):
	num_as_str = str(num)
	len_of_num = len(num_as_str)
	for i in range(len_of_num / 2):
		if num_as_str[i] != num_as_str[len_of_num - 1 - i]:
			return False
	return True


def solution():
	products = []
	for factor1 in range(999, 99, -1):
		for factor2 in range(999, 99, -1):
			product = factor1 * factor2
			if is_palindrome(product):
				products.append(product)
	return max(products)
```

OUTPUT

```shell
906609
```