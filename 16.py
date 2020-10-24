def duplicate_num(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] == arr[i+1]:
            return arr[i]

print(duplicate_num([1,3,4,2,2]))