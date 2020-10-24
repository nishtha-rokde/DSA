def sort(arr):
    sorted = []
    indexOfOne = 0
    for i in arr:
        if i == 2:
            sorted.append(i)
        elif i == 0:
            sorted.insert(0,i)
            indexOfOne += 1
        elif i == 1:
            sorted.insert(indexOfOne,i)
            indexOfOne+=1

    return sorted

print(sort([0,1,2,0,0,0,2,2,1,2,1,0,2]))


