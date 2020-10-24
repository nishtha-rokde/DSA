def subarray_sum(arr,sum_subset):
    m = len(arr)
    arr.sort()

    for j in arr:
        if j > sum_subset:
            return j
    for i in range(2,m):




