def kadane_algo(arr):
    max_so_far = 0
    max_ended_here = 0
    for i in range(len(arr)):
        max_ended_here += arr[i]
        if max_ended_here < 0:
            max_ended_here = 0
        elif max_ended_here > max_so_far:
            max_so_far = max_ended_here
    return max_so_far

print(kadane_algo([-2,-3,4,-1,2,1,3]))

