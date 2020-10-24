def common_ele(arr1,arr2,arr3):
    x,y,z = len(arr1),len(arr2),len(arr3)
    i=j=k=0
    list=[]
    while (i<x and j<y and k<z):
        if arr1[i]<arr2[j]:
            i += 1
        elif arr1[i]>arr2[j]:
            j +=1
        elif arr1[i]==arr2[j]:
            if (arr1[i] in arr3):
                list.append(arr1[i])
            i+=1
            j+=1
    return list

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
print(common_ele(ar1,ar2,ar3))

