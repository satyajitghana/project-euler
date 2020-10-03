# Number spiral diagonals

```
diagonal 1 : 1,3,7,13,21,31,43...
has a common difference of - 2,4,6,8,10,...
```

```
diagonal 2: 1,5,9,17,25,37,49,...
has a common difference of - 4,4,8,8,12,12,16...
```

```python
total_sum = 1
num = 1
num2 = 1
diagonal1 = 2
diagonal2 = 4

for i in range(1000):
    num += diagonal1
    num2+= diagonal2
    total_sum+= num + num2

    diagonal1 +=2
    if i%2!=0 and i:
        diagonal2+=4

print(total_sum)
```



OUTPUT

```
669171001
```

