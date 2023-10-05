solution = 0

#for loop to loop till 5(10-1)^5
for i in range(2,5*9**5+1):
	if sum([int(x)**5 for x in str(i)]) == i:
		solution += i

print(solution)