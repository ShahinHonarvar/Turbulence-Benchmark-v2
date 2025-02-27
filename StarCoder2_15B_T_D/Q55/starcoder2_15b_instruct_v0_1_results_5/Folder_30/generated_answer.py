from itertools import prod

def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j + 1]
            if prod(sublist) == 99:
                sublists.append(sublist)
    return sublists