def neg_to_oneside(arr):
    final_list = []
    for i in arr:
        if i<0:
            final_list.insert(0,i)
        elif i>0:
            final_list.append(i)
    return final_list

print(neg_to_oneside([2,-4,-99,98,76,-5,-1,89,4,5,6,-3,-5,-776,5,0]))

