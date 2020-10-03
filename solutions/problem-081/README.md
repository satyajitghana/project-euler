# Path sum: two ways

```py
import numpy, time

t0=time.time()

matrix = numpy.loadtxt('matrix.txt',dtype='i' ,delimiter=',')

i=0 
j=0
summm = matrix[0][0]

while i<80-1 and j < 80-1:
    if matrix[i][j+1] <= matrix[i+1][j]:
        j+=1
        summm += matrix[i][j]
        
        
    
    else:
        i+=1
        summm += matrix[i][j]
        
t1=time.time()        
print("Minimal path sum:",summm,"\nTime taken :" ,t1-t0)

```
OUTPUT:

```txt
Minimal path sum: 506297 
Time taken : 0.004987478256225586
```
