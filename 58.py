def duplicate(string_1):
    dict_1 = {}
    for c in string_1:
        if c in dict_1:
            dict_1[c] +=1
        else:
            dict_1[c] = 1
    for key,value in dict_1.items():
        if value >=2:
            print(key)


duplicate('heer')



