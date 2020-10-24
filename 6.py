def reverse(array,start,end):
    while start<end:
        array[start],array[end] = array[end],array[start]
        start = start+1
        end -=1

    return array

import numpy as np
a = np.array([1,2,3,4,5,6,7])
print(reverse(a,0,6))