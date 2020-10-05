# Lattice Paths

Starting in the top left corner of a n×m grid, and only being able to move to the right and down, all the paths are a series of down(D) and right(R)

eg. 2\*2 grid the 6 paths are: 1) DDRR 2) DRDR 3) DRRD 4) RDRD 5) RDDR 6) RRDD

so for a n\*m grid the paths are the number of ways in which n - D's and m - R's can permute

```python
from math import factorial

# grid dimensions n*m
n = 20
m = 20

number_of_paths = factorial(n+m) / ( factorial(n) * factorial(m) )

print(number_of_paths)
```

OUTPUT

```txt
137846528820
```
