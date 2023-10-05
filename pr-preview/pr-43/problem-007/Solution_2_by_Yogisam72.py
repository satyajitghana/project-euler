'''
10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

'''


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

'''
10001st prime number is: 104743
Time required: 0.021940946578979492

'''
