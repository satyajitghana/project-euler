# 10001st Prime

```Go
package main

import (
	"fmt"
	"math/big"
)

func firstNPrime(n int) int {
	var nPrime int = 0

	for i := 2; n != 0; i++ {
		if big.NewInt(int64(i)).ProbablyPrime(0) {
			nPrime = i
			n--
		}
	}

	return nPrime
}

func main() {
	fmt.Println(firstNPrime(10001))
}

```

OUTPUT

```txt
104743
```
## Python Solutions by Yogisam72
#### Solution 1

```py

import time

prime = [2]
index = 10001
prime_numbers_array_length = 1


t0 = time.time() 

i = 3
while prime_numbers_array_length != index:
    
    flag = 1
    
    for j in prime[:round(prime_numbers_array_length**0.5)]:
        if i%j == 0:
            flag = 0
            break
            
    if flag == 1:
        prime.append(i)
    
    prime_numbers_array_length = len(prime)
    
    i += 2

print("10001st prime number is:",prime[-1])

t1 = time.time() 
print("Time required:", t1 - t0) 

```
OUTPUT

```txt
10001st prime number is: 104743
Time required: 0.1237955093383789
```
#### Solution 2

```py
import time 
def SieveOfEratosthenes(n): 

    prime = [True for i in range(n+1)] 
    prime_numbers=[]
      
    p = 2
    while(p * p <= n): 
           
        # If prime[p] is not changed, then it is  
        # a prime.
        if (prime[p] == True): 
               
            # Update all multiples of p 
            for i in range(p * p, n + 1, p): 
                prime[i] = False
        p += 1
        
  
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            prime_numbers.append(p)
        
    
    return prime_numbers[10000]
      
  

t0 = time.time() 
c = SieveOfEratosthenes(110000) 
print("10001st prime number is:", c) 
  
t1 = time.time() 
print("Time required:", t1 - t0) 
```
OUTPUT:

```txt
10001st prime number is: 104743
Time required: 0.021940946578979492
```
