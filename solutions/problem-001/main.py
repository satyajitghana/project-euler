def solution(k):
	"""Sum all natural numbers that are multiples of 3 or 5, below k."""
	sum = 0
	for n in range(1, k):
		if n % 3 == 0 or n % 5 == 0:
			sum += n 
	return sum 

print(solution(1000))