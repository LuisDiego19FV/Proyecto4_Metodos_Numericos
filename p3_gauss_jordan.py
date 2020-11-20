import time
import numpy as np

t1 = time.time()

# N variables, X array of results, A matrix
n = 8
x = np.zeros(8)
a = np.array([[0.673, 1, 0, 0, 0, 0, 0, 0, 35], 
              [0.306, 0, 1, 0, 0, 0, 0, 0, 50], 
              [0.021, 0, 0, 1, 0, 0, 0, 0, 15],
              [0, 1, 0, 0, -0.059, -1, 0, 0, 0],
              [0, 0, 1, 0, -0.926, 0, -1, 0, 0],
              [0, 0, 0, 1, -0.015, 0, 0, -1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 5],
              [0, 0, 0, 0, 0, 0, 0, 1, 14]])

# Gauss Jordan Elimination
for i in range(n):

    if a[i][i] == 0.0:
        print(a)
        print('Division by zero')
        exit()
        
    for j in range(n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range(n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

# Calculate solution
for i in range(n):
    x[i] = a[i][n]/a[i][i]


t2 = time.time()

# Print solution
print('\nSolution')
for i in range(n):
    print('N%d = %0.2f' %(i+1,x[i]), end = '\n')

print("Total time: " + str(t2-t1) + "ms")
