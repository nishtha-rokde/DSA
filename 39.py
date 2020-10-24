def sum_to_palindrome(arr):
    start = 0
    end = len(arr)-1
    while start<end:
        if arr[start] == arr[end]:
            start+=1
            end-=1
        elif arr[start] > arr[end]:
            end -=1
            arr[end] +=arr[end+1]
        elif arr[start] < arr[end]:
            start+=1
            arr[start] +=arr[start-1]
    return arr

a = [1, 4, 5, 1]
c = sum_to_palindrome(a)
print(c)

