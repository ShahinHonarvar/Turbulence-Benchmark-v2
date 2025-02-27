def lists_with_product_equal_n(lst, n):
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst) + i):
            sublist = lst[i:j]
            if len(sublist) > 0 and len(sublist) <= len(lst) and (product(sublist) == n):
                sublists.append(sublist)
    return sublists

def product(lst):
    prod = 1
    for i in lst:
        prod *= i
    return prod