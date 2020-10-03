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