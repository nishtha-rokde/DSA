def choclate_dist(arr,m):
    min = max(arr)
    arr.sort()
    for i in range(len(arr)-(m-1)):
        if arr[i+m-1] - arr[i] < min:
            min = arr[i+m-1] - arr[i]
    return min

a = [12, 4, 7, 9, 2, 23, 25, 41,
30, 40, 28, 42, 30, 44, 48,
43, 50]
c = choclate_dist(a,7)
print(c)

