import numpy as np

a = np.array([range(4),range(10,14)])

b= np.array([2,-1,1,0])

print a * b

b1 = 100 * b
b2 = 100.0 * b

print b1,b2

print b1 == b2



arr = np.array([range(10)])

print arr < 3 , np.less(arr,3)

condition = np.logical_and(
