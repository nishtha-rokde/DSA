def min_swaps(arr,k):
    end = len(arr) -1
    i = 0
    while i<=end:
        if arr[i] < k:
            i +=1
        else:
