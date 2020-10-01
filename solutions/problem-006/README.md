# Sum Square Difference

Need to find : difference between (1 + 2 + 3 + .. + n)^2 - (1^2 + 2^2 + 3^2 + ... + n^2) for n = 100

t1 is (1 + 2 + 3 + .. + n)^2 
1 + 2 + ... + n is n(n+1)/2. Squaring it will give (n**4 + n**2 + 2*(n**3))/4

t2 is (1^2 + 2^2 + 3^2 + ... + n^2). Sum of n^2 is (n*(n+1)*(2*n+1))/6

putting n = 100 gives the desired answer

```
n = 100
t1 = 0.25*(n**4 + n**2 + 2*(n**3))
t2 = (n*(n+1)*(2*n+1))/6

print(int(t1-t2))
```

Output
```
25164150
```