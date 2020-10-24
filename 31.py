def max_profit(arr):
    count = 0
    start = 0
    end = 0
    while count<=2:

        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]