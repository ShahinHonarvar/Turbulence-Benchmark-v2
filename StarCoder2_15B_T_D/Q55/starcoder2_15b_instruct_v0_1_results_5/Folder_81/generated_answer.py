def lists_with_product_equal_n(lst):
    n = -8
    sublists = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] * lst[j] == n:
                sublists.append(lst[i:j + 1])
    return sublists