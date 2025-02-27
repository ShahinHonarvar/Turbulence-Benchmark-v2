def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sublist = lst[i:j]
            if len(sublist) <= n and product(sublist) == -938:
                sublists.append(sublist)
    return sublists

def product(lst):
    p = 1
    for x in lst:
        p *= x
    return p