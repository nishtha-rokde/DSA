def subarr_0(arr):
    a = 0
    while a < len(arr):
        sum = 0
        for i in range(a,len(arr)):
            sum += arr[i]
            if sum == 0:
                for j in range(a,i+1):
                    print(arr[j],end = ' ')
                print(', ',end = '')
        a+=1
ar = [-1, -3, 4, -2, 2]
print(subarr_0(ar))


