import math 

def divisible_from_1_to_n(n):  
    number = 1
    for i in range(1, n + 1):  
        number = int((number * i)/math.gcd(number, i))          
    return number 

n = int(input())
print(divisible_from_1_to_n(n))