def subset(arr1,arr2):
    for i in arr2:
        if i not in arr1:
            return False
    return True

ar1 = [11, 1, 13, 21, 3, 7]
ar2 = [11, 3, 7, 1]
res = subset(ar1,ar2)
print(res)