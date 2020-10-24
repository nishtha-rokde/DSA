def maxmin(arr,low,high):
    min = arr[low]
    max = arr[low]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
    return min,max

import numpy as np
a = np.array([1,23,4,5,6,7,45,7,22,-7])
print(maxmin(a,0,len(a)-1))