def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if len(sublist) > 0 and len(sublist) <= len(lst) and (product(sublist) == -3):
                sublists.append(sublist)
    return sublists

def product(lst):
    prod = 1
    for x in lst:
        prod *= x
    return prod