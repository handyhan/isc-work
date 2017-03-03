import numpy as np
import numpy.ma as MA

mask_arr = MA.masked_array(range(10),fill_value = -999)

print mask_arr , mask_arr.fill_value


mask_arr[2] = MA.masked

print mask_arr

print mask_arr.mask


narr = MA.masked_where(mask_arr < 6, mask_arr)

print narr, narr.fill_value

x= MA.filled(narr)

print x

print np.dtype(x)
