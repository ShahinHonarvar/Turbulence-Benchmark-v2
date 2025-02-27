def lists_with_product_equal_n(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i < j and j - i <= len(lst):
                sublist = lst[i:j]
                if len(sublist) > 0 and product(sublist) == -115:
                    yield sublist

def product(lst):
    return 1 if not lst else lst[0] * product(lst[1:])