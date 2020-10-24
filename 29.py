def longest_subsequence(arr):
    count_ended_here = 1
    count_so_far = 1

    arr.sort()
    for i in range(len(arr)):
        if i > 0 and (arr[i]-arr[i-1] == 1):
            count_ended_here += 1
            if count_ended_here > count_so_far:
                count_so_far = count_ended_here
        else:
            count_ended_here = 1
    return count_so_far

ar = [36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42]
print(longest_subsequence(ar))



