import numpy as np
x = [range(1,11)]
a1 = np.array(x,dtype=np.int32)
a2 = np.array(x, dtype=np.float32)

print a1.dtype , a2.dtype

print np.zeros(shape=(2,3,4))
print np.ones(shape=(2,3,4))

d= np.array(np.arange(0,1000))

a = np.array([2,3.2,5.5,-6.4,-2.2,2.4])

print a[1]
print a[1:4]


arr=np.array([range(4),range(10,14)])

print arr.shape, arr.size, arr.max(),arr.min()

arr=arr.reshape(2,2,2)

print arr.transpose()

print arr.ravel()
print arr.astype(np.float32)
 
