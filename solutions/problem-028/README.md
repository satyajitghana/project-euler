# Number spiral diagonals

_21_ 22 23 24 _25_
20 _7_ 8 _9_ 10
19 6 _1_ 2 11
18 _5_ 4 _3_ 12
_17_ 16 15 14 _13_

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
