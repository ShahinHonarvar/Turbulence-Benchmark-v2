def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + i + 1):
            sublist = lst[i:j]
            if len(sublist) > len(lst):
                break
            if len(sublist) > 0 and len(sublist) <= len(lst) and (product(sublist) == 714):
                sublists.append(sublist)
    return sublists

def product(lst):
    prod = 1
    for num in lst:
        prod *= num
    return prod