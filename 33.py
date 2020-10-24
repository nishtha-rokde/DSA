def triplet_sum(arr,total):

    triplets = []
    arr.sort()
    for i in range(len(arr)-2):
        start = i+1
        end = len(arr) - 1
        while start<end:
            if arr[start] + arr[end] + arr[i] > total:
                end -= 1
            elif arr[start] + arr[end]+ arr[i] < total:
                start += 1
            elif arr[start] + arr[end]+ arr[i] == total:
                triplets.append([arr[i],arr[start],arr[end]])
                start +=1
                end -= 1

    return triplets

a = [1, 2, 3, 4, 5]
c = triplet_sum(a,9)
print(c)








