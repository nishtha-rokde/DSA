def union_intersection(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    i ,j = 0,0
    union = []
    intersection = []
    while i<m and j<n:
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            union.append(arr2[j])
            j += 1
        else:
            union.append(arr1[i])
            intersection.append(arr1[i])
            i += 1
            j += 1

    while i < m:
        union.append(arr1[i])
        i +=1

    while j < n:
        union.append(arr2[j])
        j +=1

    return union,intersection

print(union_intersection([1,2,3,5,11,12,80],[3,4,5,6,9]))


