import time
import numpy as np
from numpy import array, zeros, diag, diagflat, dot

t1 = time.time()

# Matrix, sum, results
x = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]

a = np.array([[0.021, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
              [0.673, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
              [0.306, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
              [0, 0.0, 0.0, 1.0, -0.015, 0.0, 0.0, -1.0],
              [0, 0.0, 1.0, 0.0, -0.926, 0.0, -1.0, 0.0],
              [0, 1.0, 0.0, 0.0, -0.059, -1.0, 0.0, 0.0],
              [0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
              [0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])

b = [15.0, 35.0, 50.0, 0.0, 0.0, 0.0, 5.0, 14.0]

def jacobi(A, b, x, N=25):                                                                                                                                                        
                                                                                                                                                                  
    D = diag(A)
    R = A - diagflat(D)
                                                                                                                                                                        
    for i in range(N):
        x = (b - dot(R,x)) / D

    return x

solution = jacobi(a, b, x)

t2 = time.time()

print('\nSolution')
for i in range(len(solution)):
    print('N%d = %0.2f' %(i+1,solution[i]), end = '\n')

print("Total time: " + str(t2-t1) + "ms")