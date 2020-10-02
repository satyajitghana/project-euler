# Largest Product In A Series

```haskell
import Data.List

triangleNumber = scanl1 (+) [1..]

divisors n = [ d | d <- [1..(n `div` 2)], n `mod` d == 0]

numDivs = length . divisors

problem-012 = fund ((>500) . numDivs) triangleNumber
```

OUTPUT

```shell
76576500
```
