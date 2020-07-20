# Digit Factorials

```python
from functools import reduce

facts = [1] + [reduce(lambda x, y: x * y, range(1, i+1)) for i in range(1, 10)]
curi_num = lambda num: sum(map(lambda x: facts[int(x)], list(str(num)))) == num
curi_nums = [i for i in range(1000000) if curi_num(i)]
sum(set(curi_nums) - {1, 2})
```

OUTPUT

```txt
40730
```
