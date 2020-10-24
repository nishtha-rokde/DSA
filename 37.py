def partition(arr,lval,hval):
    start = 0
    end = len(arr)-1
    i=0
    while i<=end:
        if arr[i]<lval:
            temp = arr[i]
            arr[i] = arr[start]
            arr[start] = temp
            start+=1
            i+=1

        elif arr[i]>hval:
            temp = arr[i]
            arr[i] = arr[end]
            arr[end] = temp
            end -=1
        else:
            i+=1

    return arr

a = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
c = partition(a,14,20)
print(c)





