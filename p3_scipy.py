import time
import numpy as np
import scipy.linalg

t1 = time.time()

# Main matrix & right hand matrix
a = np.array([[0.673, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
              [0.306, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
              [0.021, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
              [0, 1.0, 0.0, 0.0, -0.059, -1.0, 0.0, 0.0],
              [0, 0.0, 1.0, 0.0, -0.926, 0.0, -1.0, 0.0],
              [0, 0.0, 0.0, 1.0, -0.015, 0.0, 0.0, -1.0],
              [0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
              [0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])

b = [35.0, 50.0, 15.0, 0.0, 0.0, 0.0, 5.0, 14.0]

solution = scipy.linalg.solve(a,b)

t2 = time.time()

print('\nSolution')
for i in range(len(solution)):
    print('N%d = %0.2f' %(i+1,solution[i]), end = '\n')

print("Total time: " + str(t2-t1) + "ms")

