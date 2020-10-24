def max_product(arr):
    a = 0
    product_so_far = 1
    product_ended_here = 1
    while a<len(arr):
        for i in range(a,len(arr)):
            product_ended_here *= arr[i]
            if product_ended_here > product_so_far:
                product_so_far = product_ended_here
    return product_so_far

ar = [6, -3, -10]
print(max_product(ar))
