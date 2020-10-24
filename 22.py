def stocks(arr):
    start = arr[0]
    end = arr[-1]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] < arr[j]:
                if start > arr[i]:
                    start = arr[i]
                if end < arr[j]:
                    end = arr[j]
    profit = end-start
    return profit

    print(stocks([7,1,5,3,6,4]))

