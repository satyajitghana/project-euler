# Self Powers

We need to find the last 10 digits of a sum that i given by 1^1 + 2^2 + 3^3 + ...  uptp 1000^1000

the num%10000000000 gives us remainder after dividing by 10000000000 which is the required answer

```python
num = 0

for i in range(1,1001):
    num = num + i**i
    
print(num%10000000000)
```

Output

```
9110846700
```
