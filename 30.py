def find_all_nums(arr,k):
    num = int(len(arr)/k)
    dict1 = {}

    for i in arr:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1

    for key,value in dict1.items():
        if value > num:
            print(key)

ar = [3, 1, 2, 2, 1, 2, 3, 3]
find_all_nums(ar,4)




















#     count = 1
#     p = False
#     arr.sort()
#     for i in range(1,len(arr)):
#         if arr[i] - arr[i-1] == 0:
#             count+=1
#             if count>c and p = False:
#                 print(arr[i])
#                 p = True
#         else:
#             count = 1
#             p = False
#
# ar = [3,1,2,2,2,1,4,3,3]
# print(find_all(ar,4))





