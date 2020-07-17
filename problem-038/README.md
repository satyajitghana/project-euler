# Pandigital Multiples

```python
from functools import reduce

def concat_prod(x, l):
    return reduce(lambda x, y: x + y, [str(num * x) for num in l])
    
digitset = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
pandigitalnums = [(int(concat_prod(x, l)), x) for x in range(9000, 9999) if set(concat_prod(x, l)) == digitset]

pandigitalnums
```

OUTPUT

```txt
[(926718534, 9267), (927318546, 9273), (932718654, 9327)]
932718654
```
