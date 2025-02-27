def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i, i + n):
            sublist = lst[i:j]
            if len(sublist) > 0 and len(sublist) <= n and (-61 % product(sublist) == 0):
                sublists.append(sublist)
    return sublists

def product(lst):
    p = 1
    for x in lst:
        p *= x
    return p