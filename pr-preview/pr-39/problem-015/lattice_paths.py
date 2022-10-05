from math import factorial

# grid dimensions n*m
n = 20
m = 20

number_of_paths = factorial(n+m) / ( factorial(n) * factorial(m) )

print(number_of_paths)
