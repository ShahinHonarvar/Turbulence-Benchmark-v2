def lists_with_product_equal_n(lst):
    n = -18
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) <= len(lst) and len(sublist) > 0 and (product(sublist) == n):
                sublists.append(sublist)
    return sublists

def product(lst):
    p = 1
    for x in lst:
        p *= x
    return p