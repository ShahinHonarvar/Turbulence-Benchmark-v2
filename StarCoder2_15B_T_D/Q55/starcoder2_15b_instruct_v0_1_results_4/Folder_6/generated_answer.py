def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        for j in range(i, i + n):
            k = j % n
            sublist = lst[i:k + 1]
            if len(sublist) > 0 and len(sublist) <= n and (product(sublist) == 42):
                sublists.append(sublist)
    return sublists

def product(lst):
    p = 1
    for x in lst:
        p *= x
    return p