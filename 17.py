import numpy as np
def merge_arr(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    arr3 = [] * (n+m)
    arr3 = arr1+arr2
    arr3.sort()
    return arr3
a = [2, 4, 6, 8,9]
b = [1, 3, 5, 7,8]
print(merge_arr(a,b))

