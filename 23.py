def arr_sum(arr,sum):
    arr.sort()
    start = 0
    end = len(arr) - 1
    list = []
    count = 0
    while start < end:
        if (arr[start] + arr[end]) < sum:
            start +=1
        elif (arr[start] + arr[end]) > sum:
            end -= 1
        elif (arr[start] + arr[end]) == sum:
            list.append([arr[start], arr[end]])
            count += 1
            start+=1
            end-=1


    return list,count

print(arr_sum([1,5,7,-1],6))
