def lists_with_product_equal_n(lst):
    n = 91
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            prod = 1
            for k in range(i, j % len(lst) + i):
                prod *= lst[k]
            if prod == n:
                sublists.append(lst[i:j % len(lst) + i])
    return sublists