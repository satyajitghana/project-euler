# Darts

```python
limit = 100
result = 0
scores = []
# build all possible single dart scores

for i in range(1,21):
    scores.append(i)
    scores.append(2 * i)
    scores.append(3 * i)

scores.append(25)
scores.append(50)

#make all the possible doubles

doubles =[]
for i in range(1,21):
    doubles.append(2 * i)

doubles.append(25 * 2)

#Count all miss, miss, double

for third in doubles:
    if (third < limit):
        result=result+1


#count all miss, hit, double
for i in range(len(scores)):
    for third in doubles:
        if scores[i] + third < limit:
            result=result+1
    


#count all hit, hit, double
for i in range(len(scores)):
    for j in range(i,len(scores)):
        for third in doubles:
            if (scores[i] + scores[j] + third < limit):
                result=result+1

result
```

OUTPUT

```txt
  38182
```