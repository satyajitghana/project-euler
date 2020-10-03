'''

10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

'''


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




'''

OUTPUT:
10001st prime number is: 104743
Time required: 0.1237955093383789

'''
